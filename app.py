import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.post import *
from lib.post_repository import *
from lib.user import *
from lib.user_repository import *
from datetime import datetime


app = Flask(__name__)

@app.route('/chitter/homepage', methods = ['GET'])
def get_posts():
    connection = get_flask_database_connection(app)
    repo = PostRepository(connection)
    repo2 = UserRepository(connection)
    posts = repo.all()
    for post in posts:
        post.user_id = repo2.find_username(post.user_id)
        post.added_on = post.added_on.strftime('%d/%m/%Y, %H:%M')
    return render_template('homepage.html', posts = posts[::-1])

@app.route('/chitter/homepage', methods = ['POST'])
def send_peep():
    connection = get_flask_database_connection(app)
    repo = PostRepository(connection)
    content = request.form['content']
    #actual
    #added_on = datetime.now()
    #test
    added_on = datetime(2023,12,6,12,0)
    user_id = 1
    post = Post(None,content,user_id,added_on)
    if not post.is_valid():
        return render_template('homepage.html', errors = post.generate_errors(), post = post)
    repo.create(post)
    return redirect('/chitter/homepage')

@app.route('/chitter/sign_up', methods = ['GET'])
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/chitter/sign_up', methods = ['POST'])
def sign_up():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    username = request.form['username']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    user = User(None,username,first_name,last_name,email,password)
    if not user.is_valid():
        return render_template('sign_up.html', user = user, errors = user.generate_errors()), 400
    if repo.user_exists(username):
        return render_template('sign_up.html', user = user, errors = 'This username already exists. Please choose an alternative.'),400
    user = repo.add(user)
    return redirect(f'/chitter/{user.id}')
    
@app.route('/chitter/<int:id>', methods=['GET'])
def get_user_page(id):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find(id)
    return render_template('user.html', user = user)

if __name__ == '__main__':
    app.run(debug=True, port = int(os.environ.get('PORT', 5001)))