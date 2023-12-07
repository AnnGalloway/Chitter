from lib.post import *
from datetime import datetime

post1 = Post(1,"content",1,datetime(2023,12,1,12))

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