from lib.user import User
from lib.user_repository import *

def test_find_username(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    result = repository.find_username(1)
    assert result == 'user1'

def test_user_exists(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    result = repository.user_exists('user1')
    assert result == True

def test_user_not_exists(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    result = repository.user_exists('user3')
    assert result == False

def test_show_users(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    users = repository.show_users()
    assert users == [
        User(1,'user1', 'fname1', 'lname1', 'email1@email.com', 'password1'),
        User(2,'user2', 'fname2', 'lname2', 'email2@email.com', 'password2')
    ]

def test_add_user(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    user = User(None,'user3', 'fname3', 'lname3', 'email3@email.com', 'password3')
    repository.add(user)
    users = repository.show_users()
    assert users == [
        User(1,'user1', 'fname1', 'lname1', 'email1@email.com', 'password1'),
        User(2,'user2', 'fname2', 'lname2', 'email2@email.com', 'password2'),
        User(3,'user3', 'fname3', 'lname3', 'email3@email.com', 'password3')
    ]

def test_find(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1,'user1', 'fname1', 'lname1', 'email1@email.com', 'password1')