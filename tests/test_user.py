from lib.user import User

def test_user_initialises_correctly():
    user = User(1, "name", "email", "password")
    assert user.id == 1
    assert user.name == "name"
    assert user.email == "email"
    assert user.password == "password"

def test_users_are_the_same():
    user1 = User(1, "name", "email", "password")
    user2 = User(1, "name", "email", "password")
    assert user1 == user2

def test_user_formats_correctly():
    user = User(1, "name", "email", "password")
    assert str(user) == "User(1, name, email, password)"
