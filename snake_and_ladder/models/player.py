class Player:
    id_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = Player.id_counter
        Player.id_counter = Player.id_counter + 1

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id
