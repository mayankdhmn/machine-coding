from services.owe_book_service import OweBookService

class ParseAndSimulate():
    def __init__(self, owe_book_service):
        self.owe_book_service = owe_book_service

    def simulate(self, file_name):
        with open(file_name, 'r') as f:
            inp_lines = f.readlines()
            for inp in inp_lines:
                inp = inp.strip().split()
                print(inp)
                if inp[0] == 'SHOW':
                    if len(inp) == 1:
                        balances = self.owe_book_service.get_balance_all()
                    else:
                        user_id = str(inp[1])
                        balances = self.owe_book_service.get_balance(user_id)
                    if not balances:
                        print('No balances')
                    for balance in balances:
                        print(str(balance))
                elif inp[0] == 'EXPENSE':
                    user_paying = int(inp[1])
                    amount_paid = inp[2]
                    divided_among = int(inp[3])
                    users_divided_in = list(map(int, inp[4:4 + divided_among]))
                    division_type_and_params = inp[4 + divided_among:]
                    self.owe_book_service.update_balances(user_paying, int(amount_paid), users_divided_in, division_type_and_params)
                else:
                    print('Invalid Input :-/') 
        