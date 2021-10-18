from models.id_to_user_mapping import IDToUserMapping

class Balance():
    def __init__(self, user1, user2, amount):
        self.user1 = user1
        self.user2 = user2
        self.amount = amount

    def __str__(self):
        return f'{IDToUserMapping.get_user(self.user1)} owes {IDToUserMapping.get_user(self.user2)}: {self.amount}'