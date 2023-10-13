from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = [User(row['id'], row['name'], row['email'], row['password']) for row in rows]
        return users

    def find_by_user_id(self, user_id):
        row = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        user = User(row[0]['id'], row[0]['name'], row[0]['email'], row[0]['password'])
        return user

    def find_by_user_email(self, user_email):
        row = self._connection.execute('SELECT * FROM users WHERE email = %s', [user_email])
        user = User(row[0]['id'], row[0]['name'], row[0]['email'], row[0]['password'])
        return user

    def add_user(self, user):
        record = self._connection.execute('INSERT INTO users (name, email, password) VALUES '
                                        '(%s, %s, %s) RETURNING id', [user.name, user.email, user.password])
        return record[0]['id']
