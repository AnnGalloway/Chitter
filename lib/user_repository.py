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