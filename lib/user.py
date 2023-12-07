class User:
    def __init__(self, id, username, name, email, password):
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.name}, {self.email}, {self.password})'