class User:
    def __init__(self, id, username, first_name, last_name, email, password):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.first_name} {self.last_name}, {self.email})'
    
    def is_valid(self):
        if self.username == '' or self.username == None:
            return False
        if self.first_name == '' or self.first_name == None:
            return False
        if self.last_name == '' or self.last_name == None:
            return False
        if self.email == '' or self.email == None:
            return False
        if self.password == '' or self.password == None:
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.username == '' or self.username == None:
            errors.append("Username cannot be blank")
        if self.first_name == '' or self.first_name == None:
            errors.append("First name cannot be blank")
        if self.last_name == '' or self.last_name == None:
            errors.append("Last name cannot be blank")
        if self.email == '' or self.email == None:
            errors.append("E-mail cannot be blank")
        if self.password == '' or self.password == None:
            errors.append("Password cannot be blank")
        if len(errors) == 0:
            return None
        return ', '.join(errors)