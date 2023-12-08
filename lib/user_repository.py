from lib.user import *

class UserRepository:
    def __init__(self,connection):
        self._connection = connection

    def find_username(self,id):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE id = %s',[id]
        )
        row = rows[0]
        return row['username']
    
    def user_exists(self,username):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE username = %s',[username]
        )
        if rows == []:
            return False
        return True
    
    def show_users(self):
        rows = self._connection.execute(
            "SELECT * FROM users"
        )
        users = []
        for row in rows:
            user = User(row['id'], row['username'], row['first_name'], row['last_name'], row['email'], row['password'])
            users.append(user)
        return users

    
    def add(self, user):
        rows = self._connection.execute(
            'INSERT INTO users (username, first_name, last_name, email, password) '\
            'VALUES (%s,%s,%s,%s,%s) RETURNING id',[
                user.username, user.first_name, user.last_name, user.email, user.password
            ])
        row = rows[0]
        user.id = row['id']
        return user
    
    def find(self,id):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE id = %s',[id]
        )
        row = rows[0]
        return User(row['id'], row['username'], row['first_name'], row['last_name'], row['email'], row['password'])
        