from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")

'''
When we visit the home page,
we should see a welcome message
'''
def test_welcome_message_displays(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Welcome to MakersBnB!")

def test_welcome_buttons(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    buttons = page.locator('.t-buttons')
    expect(buttons).to_have_text('Login\nSign-up')

def test_click_signup_button(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    header = page.locator('.t-header')
    expect(header).to_have_text('Sign up to MakersBNB')
    email = page.locator('.t-email')
    expect(email).to_have_text('Email address:')
    password = page.locator('.t-password')
    expect(password).to_have_text('Password:')
    confirm_password = page.locator('.t-confirm_password')
    expect(confirm_password).to_have_text('Confirm password:')


def test_click_homepage_login_button(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    header = page.locator('.t-header')
    expect(header).to_have_text('Please Login')
    email = page.locator('.t-email')
    expect(email).to_have_text('Email address:')
    password = page.locator('.t-password')
    expect(password).to_have_text('Password:')

def test_sign_up_page_enter_invalid_email_address(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "ksfuhoief")
    page.click("text='Sign-up'")
    error = page.locator('.error')
    expect(error).to_have_text('ksfuhoief is not a valid email address')

def test_sign_up_page_enter_invalid_password(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "m.@o")
    page.fill("input[name=password]", "lkfek")
    page.click("text='Sign-up'")
    errors = page.locator('.error')
    expect(errors).to_have_text(['Password must be at least 8 characters.', 
                                'Password must contain uppercase and lowercase characters.',
                                'Password must contain at least 1 number.', 
                                'Password must contain at least 1 symbol.' 
])

def test_sign_up_page_enter_non_identical_passwords(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "m.@o")
    page.fill("input[name=password]", "Makersbnbpassword!23")
    page.fill("input[name=confirm_password]", "aaaa")
    page.click("text='Sign-up'")
    error = page.locator('.error')
    expect(error).to_have_text('passwords do not match')

def test_sign_up_page_goes_through_to_available_spaces_page(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "m.@o")
    page.fill("input[name=password]", "Makersbnbpassword!23")
    page.fill("input[name=confirm_password]", "Makersbnbpassword!23")
    page.click("text='Sign-up'")
    header = page.locator('h1')
    expect(header).to_have_text('Available Spaces')


def test_login_page_email_address_and_password_missing(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    page.click("text='Login'")
    error = page.locator('.error')
    expect(error).to_have_text("Please enter your email address and password")

    # p_tag = page.locator('p')
    # expect(p_tag).to_have_text('Test Available Spaces')

'''
When we go to List New Space
we should see a page with fields
for the user to enter details of the space
that match the Space object properties
'''

def test_new_space_page_displays(page, test_web_address):
    page.goto(f'http://{test_web_address}/new-space')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Enter new space details')

'''
When we click the field with the appropriate attribute
we can add that detail to the form
'''
## DESCOPED
# def test_add_new_space_with_attribute_details(page, test_web_address, db_connection):
#     db_connection.seed('seeds/makersbnb.sql')
#     page.goto(f'http://{test_web_address}/new-space')
#     page.fill('text=Space Name', 'Test new space')
#     # page.fill('text=Description', 'Test description')
#     # page.fill('text=Start date', '2023-03-01')
#     # page.fill('text=End date', '2023-03-15')
#     # page.fill('text=Price per night', 2000)

#     page.click('text=Add new space')
#     name_element = page.locator('.t-name')
#     expect(name_element).to_have_text('Test new space')
    


def test_login_page_email_address_not_found(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    page.fill("input[name=email]", "m.@o")
    page.click("text='Login'")
    error = page.locator('.error')
    expect(error).to_have_text("Email address not found")

def test_login_page_password_missing(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    page.fill("input[name=email]", "user1@email.com")
    page.click("text='Login'")
    error = page.locator('.error')
    expect(error).to_have_text("Please enter your password")

def test_login_page_contains_incorrect_password(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    page.fill("input[name=email]", "user1@email.com")
    page.fill("input[name=password]", "kajgfhsalk")
    page.click("text='Login'")
    error = page.locator('.error')
    expect(error).to_have_text("Incorrect password")

def test_login_page_goes_through_to_available_spaces(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    page.fill("input[name=email]", "user1@email.com")
    page.fill("input[name=password]", "password1")
    page.click("text='Login'")
    header = page.locator('h1')
    expect(header).to_have_text('Available Spaces')


# The test below is related to the POST route in app.py. This relies on further functionality
# in the login procedure. Perhaps this can be implemented at a later date.

# def test_new_booking(page, test_web_address):
#     page.goto(f'http://{test_web_address}/')
#     page.click("text='Login'")
#     page.click("text='Login'")
#     page.click("id='3'")
#     page.fill("input[checkin]", "2030-01-15")
#     page.fill("input[checkout]", "2030-01-20")
#     page.click("text='Book'")


