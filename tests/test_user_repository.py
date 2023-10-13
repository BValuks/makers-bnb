from lib.user_repository import UserRepository
from lib.user import User

def test_get_all(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    result = repo.get_all()
    assert result == [
        User(1, 'user1', 'user1@email.com', 'password1'),
        User(2, 'user2', 'user2@email.com', 'password2')
    ]

def test_find_by_user_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    result = repo.find_by_user_id(1)
    assert result == User(1, 'user1', 'user1@email.com', 'password1')

def test_find_by_user_email(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    result = repo.find_by_user_email("user2@email.com")
    assert result == User(2, 'user2', 'user2@email.com', 'password2')

def test_add_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    user3 = User(None, 'user3', 'user3@email.com', 'password3')
    assert repo.add_user(user3) == 3
    assert repo.get_all() == [
        User(1, 'user1', 'user1@email.com', 'password1'),
        User(2, 'user2', 'user2@email.com', 'password2'),
        User(3, 'user3', 'user3@email.com', 'password3')
    ]
