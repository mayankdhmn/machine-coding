class OweBook:
    """A Record of how much one person owes other person
    """

    def __init__(self, user_ids):
        self.owe_book_dict = {}
        for user_id_1 in user_ids:
            for user_id_2 in user_ids:
                if user_id_1 != user_id_2:
                    self.owe_book_dict[(user_id_1, user_id_2)] = 0
                    self.owe_book_dict[(user_id_2, user_id_1)] = 0


