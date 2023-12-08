from lib.post import *
from datetime import datetime

post1 = Post(1,"content",1,datetime(2023,12,1,12))
long = '1'*165

def test_init():
    assert post1.id == 1
    assert post1.content == 'content'
    assert post1.user_id == 1
    assert post1.added_on == datetime(2023,12,1,12)


def test_same():
    post2 = Post(1,"content",1, datetime(2023,12,1,12))
    assert post1 == post2

def test_display():
    assert str(post1) == 'Post(1, content, 1, 2023-12-01 12:00:00)'

def test_is_valid():
    assert Post(1,'','',datetime(2023,12,1,12)).is_valid() == False
    assert Post(1,'content','',datetime(2023,12,1,12)).is_valid() == False
    assert Post(1,'','user',datetime(2023,12,1,12)).is_valid() == False
    assert Post(1,long,'user',datetime(2023,12,1,12)).is_valid() == False
    assert Post(1,'content','user',datetime(2023,12,1,12)).is_valid() == True
    assert Post(None,'content','user',datetime(2023,12,1,12)).is_valid() == True

def test_errors():
    assert Post(1,'','',datetime(2023,12,1,12)).generate_errors() == "You can't send a blank Peep, Please log in to send a Peep"
    assert Post(1,'content','',datetime(2023,12,1,12)).generate_errors() == "Please log in to send a Peep"
    assert Post(1,'','user',datetime(2023,12,1,12)).generate_errors() == "You can't send a blank Peep"
    assert Post(1,long,'user',datetime(2023,12,1,12)).generate_errors() == "Maximum length of a Peep is 160 characters"
    assert Post(1,'content','user',datetime(2023,12,1,12)).generate_errors() == None
    assert Post(None,'content','user',datetime(2023,12,1,12)).generate_errors() == None