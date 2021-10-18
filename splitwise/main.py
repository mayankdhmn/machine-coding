from models.owe_book import OweBook
from models.user import User
from models.id_to_user_mapping import IDToUserMapping

from services.owe_book_service import OweBookService
from services.parse_simulate_service import ParseAndSimulate

def main():
    u1 = User(name='Mayank', email='md@m.com', mobile_number='123')
    u2 = User(name='Lavish', email='we@m.com', mobile_number='42')
    u3 = User(name='Bill', email='wd@m.com', mobile_number='81')
    u4 = User(name='Scott', email='scott@m.com', mobile_number='18')
    users = [u1, u2, u3, u4]
    user_ids = list(map(lambda x : x.get_id(), users))
    IDToUserMapping(users)
    owe_book_service = OweBookService(OweBook(user_ids))
    parse_and_simulate = ParseAndSimulate(owe_book_service)
    parse_and_simulate.simulate('input.txt')

if __name__ == '__main__':
    main()