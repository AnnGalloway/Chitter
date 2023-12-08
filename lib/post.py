class Post:
    def __init__(self,id,content,user_id, added_on):
        self.id = id
        self.content = content
        self.user_id = user_id
        self.added_on = added_on
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Post({self.id}, {self.content}, {self.user_id}, {self.added_on})'
    
    def is_valid(self):
        if self.content == '' or self.content == None:
            return False
        if len(self.content) > 160:
            return False
        if self.user_id == '' or self.user_id == None:
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.content == '' or self.content == None:
            errors.append('You can\'t send a blank Peep')
        if len(self.content) > 160:
            errors.append('Maximum length of a Peep is 160 characters')
        if self.user_id == '' or self.user_id == None:
            errors.append('Please log in to send a Peep')
        if len(errors) == 0:
            return None
        return ', '.join(errors)