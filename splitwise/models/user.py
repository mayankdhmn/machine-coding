class User():
    id = 0

    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.id = User.id
        User.id += 1
    
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email
    
    def get_mobile_number(self):
        return self.mobile_number