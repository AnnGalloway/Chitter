from lib.post import *
import datetime

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM posts'
        )
        posts = []
        for row in rows:
            post = Post(row['id'],row['content'],row['user_id'], row['added_on'])
            posts.append(post)
        return posts

    def create(self, post):
        rows = self._connection.execute(
            'INSERT INTO posts (content, user_id, added_on) VALUES (%s,%s,%s) RETURNING id',
            [post.content, post.user_id, post.added_on]
        )
        row = rows[0]
        post.id = row['id']
        return post
    
