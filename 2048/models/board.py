from random import randint
from models.tile import Tile

class Board:
    def __init__(self):
        self.size = 4
        self.grid = [[None] * self.size for _ in range(self.size)]

        rand_index1_i, rand_index1_j = self.get_random_index()
        rand_index2_i, rand_index2_j = self.get_random_index()
        while rand_index1_i == rand_index2_i and rand_index1_j == rand_index2_j:
            rand_index2_i, rand_index2_j = self.get_random_index()

        rand_val1 = self.get_random_tile_value()
        rand_val2 = self.get_random_tile_value()

        self.grid[rand_index1_i][rand_index1_j] = Tile(rand_val1, False)
        self.grid[rand_index2_i][rand_index2_j] = Tile(rand_val2, False)
        

    def get_random_index(self):
        return (randint(0, self.size() - 1), randint(0, self.size() - 1))
    
    def get_random_tile_value(self):
        return pow(2, randint(1, 3))

    def insert_random_tile(self):
        rand_index_i, rand_index_j = self.get_random_index()
        while self.grid[rand_index_i][rand_index_j] is not None:
            rand_index_i, rand_index_j = self.get_random_index()
        self.grid[rand_index_i][rand_index_j] = Tile(self.get_random_tile_value(), False)

    def display_board(self):
        """Displays the board

        Arguments:
            None
        
        Returns:
            None
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] is not None:
                    print(self.grid[i][j].get_value(), end=' ')
                else:
                    print('-', end=' ')
            print('\n')
        
    def get_game_status(self):
        count_empties = 0
        for i in range(self.size):
            for j in range(self.size):
                if not self.grid[i][j]:
                    count_empties = count_empties + 1
                elif self.grid[i][j].get_value() == 2048:
                    return 'WON'
        if count_empties == 0:
            return 'OVER'
        else:
            return 'UNDECIDED'