from lib.user import *

user1 = User(1, 'username1', 'bob smith', '123@123.com', 'password123')

def test_init():
    assert user1.id == 1
    assert user1.username == 'username1'
    assert user1.name == 'bob smith'
    assert user1.email == '123@123.com'
    assert user1.password == 'password123'

def test_same():
    user2 = User(1, 'username1', 'bob smith', '123@123.com', 'password123')
    assert user1 == user2

def test_display():
    assert str(user1) == 'User(1, username1, bob smith, 123@123.com, password123)'
