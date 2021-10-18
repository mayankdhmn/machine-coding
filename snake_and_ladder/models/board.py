class Board:
    def __init__(self, board_size, snakes, ladders):
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders

        self.snake_mapping, self.ladder_mapping = {}, {}
        for snake in snakes:
            self.snake_mapping[snake.get_start()] = snake.get_end()
        
        for ladder in ladders:
            self.ladder_mapping[ladder.get_start()] = ladder.get_end()

    def get_size(self):
        return self.board_size
        
    # def total_roll(self):
    #     roll_count = 0
    #     for die in self.dies:
    #         roll_count = roll_count + die.roll()
    #     return roll_count
