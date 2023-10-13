import os
from flask import Flask, request, render_template, redirect, flash
from lib.database_connection import get_flask_database_connection
import re
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from flask_login import LoginManager, login_user, logout_user, current_user
from lib.space import Space
from lib.booking_repository import BookingRepository
from lib.booking import Booking

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
login_manager = LoginManager()
login_manager.init_app(app)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    return repo.find_by_user_id(user_id)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect('/')

def is_valid_email(email):
    return "@" in email and "." in email

def check_valid_password(password):
    validation_messages = []
    if len(password) < 8:
        validation_messages.append('Password must be at least 8 characters.')
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        validation_messages.append('Password must contain uppercase and lowercase characters.')
    if not any(char.isdigit() for char in password):
        validation_messages.append('Password must contain at least 1 number.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        validation_messages.append('Password must contain at least 1 symbol.')
    if not validation_messages:
        return True
    else:
        return validation_messages

def passwords_match(password, confirm_password):
    return password == confirm_password

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/sign_up', methods=['POST'])
def signup(): 
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    name = request.form['name']
    email_address = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if not is_valid_email(email_address):
        flash(f"{email_address} is not a valid email address","error")
        return redirect('/signup')
    password_is_valid = check_valid_password(password)
    if password_is_valid != True:
        for error in password_is_valid:
            flash(error, "error")
        return redirect('/signup')
    if not passwords_match(password, confirm_password):
        flash("passwords do not match", "error")
        return redirect('/signup')
    user = User(None, name, email_address, password)
    id = repo.add_user(user)
    user.id = id
    login_user(user)
    return redirect('/available-spaces')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    email_address = request.form['email']
    password = request.form['password']
    all_users = user_repo.get_all()
    user_email_addresses = [user.email for user in all_users]
    if email_address == "" or email_address == None:
        flash("Please enter your email address and password", "error")
        return redirect('/login')
    if email_address not in user_email_addresses:
        flash("Email address not found", "error")
        return redirect('/login')
    if password == "" or password == None:
        flash("Please enter your password", "error")
        return redirect('/login')
    user = user_repo.find_by_user_email(email_address)
    if user.password != password:
        flash("Incorrect password", "error")
        return redirect('/login')

    if isinstance(user.id, int):
        login_user(user)
        return redirect('/available-spaces')
    return redirect('/login')

@app.route('/available-spaces', methods=['GET'])
def get_available_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('available_spaces.html', spaces = spaces, current_user = current_user)

'''
GET /new-space
Returns heading
'Enter new space details'
'''
@app.route('/new-space', methods=['GET'])
def add_new_space():
    return render_template('new_space.html')

@app.route('/new-space', methods=['POST'])
def post_new_space():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    name = request.form['space_name']
    description = request.form['description']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    price = request.form['price']
    space = Space(None, name, description, start_date, end_date, price, current_user.id)
    repo.add_space(space)
    return redirect('/new-space-confirmation')


@app.route('/space/<int:id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    matching_space = [space for space in spaces if space.id == id]
    return render_template('space_page.html', matching_space = matching_space[0], current_user = current_user)

@app.route('/space/<int:id>', methods=['POST'])
def post_newbooking(id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    start_date = request.form['checkin']
    end_date = request.form['checkout']
    user_id = current_user.id
    space_id = id
    repo.create(Booking(None, start_date, end_date, user_id, space_id))
    return redirect('/newbooking')

@app.route('/newbooking', methods=['GET'])
def get_newbooking():
    return render_template('newbooking.html')

@app.route('/new-space-confirmation', methods=['GET'])
def get_space_confirmation():
    return render_template('new_space_confirmation.html')

@app.route('/myaccount', methods=['GET'])
def get_myaccount():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    booking_repo = BookingRepository(connection)
    spaces = space_repo.find_by_user_id(current_user.id)
    bookings = booking_repo.find_by_user(current_user.id)
    booking_spaces = [space_repo.find_by_space_id(booking.space_id) for booking in bookings]
    return render_template('myaccount.html', spaces=spaces, bookings=bookings, booking_spaces=booking_spaces)

# Post route below was for making a new booking. This relied on extra functionality
# around user login. Perhaps this can be implemented at a later date

# @app.route('/newbooking', methods=['POST'])
# def post_new_booking():
#     connection = get_flask_database_connection(app)
#     repo = BookingRepository(connection)
#     start_date = request.form['checkin']
#     end_date = request.form['checkout']


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
