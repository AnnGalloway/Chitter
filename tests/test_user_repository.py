from lib.user import User
from lib.user_repository import *

def test_find_username(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    result = repository.find_username(1)
    assert result == 'user1'