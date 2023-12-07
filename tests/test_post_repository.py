from lib.post import *
from lib.post_repository import *
from datetime import datetime

def test_show_all(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post(1,'post1', 1, datetime(2023,12,1,12)),
        Post(2,'post2', 1, datetime(2023,12,2,12)),
        Post(3,'post3', 2, datetime(2023,12,3,12)),
        Post(4,'post4', 2, datetime(2023,12,4,12)),
        Post(5,'post5', 1, datetime(2023,12,5,12))
    ]

def test_create(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PostRepository(db_connection)
    post = Post(None,'post6',2, datetime(2023,12,6,12))
    repository.create(post)
    posts = repository.all()
    assert posts == [
        Post(1,'post1', 1, datetime(2023,12,1,12)),
        Post(2,'post2', 1, datetime(2023,12,2,12)),
        Post(3,'post3', 2, datetime(2023,12,3,12)),
        Post(4,'post4', 2, datetime(2023,12,4,12)),
        Post(5,'post5', 1, datetime(2023,12,5,12)),
        Post(6,'post6', 2, datetime(2023,12,6,12))
    ]