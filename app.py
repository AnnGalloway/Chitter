import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.post import *
from lib.post_repository import *
from lib.user import *
from lib.user_repository import *


app = Flask(__name__)

@app.route('/homepage', methods = ['GET'])
def get_posts():
    connection = get_flask_database_connection(app)
    repo = PostRepository(connection)
    repo2 = UserRepository(connection)
    posts = repo.all()
    for post in posts:
        post.user_id = repo2.find_username(post.user_id)
    return render_template('homepage.html', posts = posts[::-1])

if __name__ == '__main__':
    app.run(debug=True, port = int(os.environ.get('PORT', 5001)))