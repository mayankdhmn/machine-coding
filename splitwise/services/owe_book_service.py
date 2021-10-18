from models.balance import Balance

class OweBookService():
    def __init__(self, owe_book):
        self.owe_book = owe_book

    def get_balance_all(self):
        balances = [] 
        for pair, amount in self.owe_book.owe_book_dict.items():
            amount -= self.owe_book.owe_book_dict[(pair[1], pair[0])]
            if amount > 0:
                balance = Balance(pair[0], pair[1], amount)
                balances.append(balance)
        return balances

    def get_balance(self, user):
        balances = []
        for pair, amount in self.owe_book.owe_book_dict.items():
            amount -= self.owe_book.owe_book_dict[(pair[1], pair[0])]
            if amount > 0 and (pair[0] is user or pair[1] is user):
                balance = Balance(pair[0], pair[1], amount)
                balances.append(balance)
        return balances

    def update_balances(self, user_paying, amount_paid, users_divided_in, division_type_and_params):
        updated_successfully = True
        if division_type_and_params[0] == 'EQUAL':
            amount_divided = amount_paid / len(users_divided_in)
            for user in users_divided_in:
                if user is not user_paying:
                    self.owe_book.owe_book_dict[(user, user_paying)] += amount_divided
        elif division_type_and_params[0] == 'EXACT':
            params = list(map(int, division_type_and_params[1:]))
            for i in range(len(users_divided_in)):
                if users_divided_in[i] is not user_paying:
                    self.owe_book.owe_book_dict[(users_divided_in[i], user_paying)] += params[i]
        elif division_type_and_params[0] == 'PERCENT':
            percentages = list(map(int, division_type_and_params[1:]))
            if sum(percentages) != 100:
                updated_successfully = False
            else:
                for i in range(len(users_divided_in)):
                    if users_divided_in[i] is not user_paying:
                        self.owe_book.owe_book_dict[(users_divided_in[i], user_paying)] += percentages[i] * amount_paid / 100
        else:
            updated_successfully = False
        return updated_successfully