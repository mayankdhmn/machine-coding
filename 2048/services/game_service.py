class Game:
    def __init__(self, board):
        self.board = board
    
    def play(self):
        """Play the simulation

        Arguments:
            None
        
        Returns:
            None
        """
        while self.board.get_game_status() == 'UNDECIDED':
            self.board.display_board()
            move_direction = int(input('Enter your move:'))
            if move_direction == 0:
                self.move_left()
            elif move_direction == 1:
                self.move_right()
            elif move_direction == 2:
                self.move_top()
            elif move_direction == 3:
                self.move_down()
            self.board.insert_random_tile()
        game_status = self.board.get_game_status()
        self.board.display_board()
        if game_status == 'WON':
            print("Congratulations")
        elif game_status == 'OVER':
            print('Game Over')
        
    def move_right(self):
        for i in range(self.board.size):
            temp_row = []
            for j in range(self.board.size - 1, -1, -1):
                if not self.board.grid[i][j]:
                    continue
                if len(temp_row) == 0:
                    temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() == self.board.grid[i][j].get_value():
                    if not temp_row[-1].is_merged_once():
                        temp_row[-1].set_value(temp_row[-1].get_value() * 2)
                        temp_row[-1].set_merged_once(True)
                    else:
                        temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() != self.board.grid[i][j].get_value():
                    temp_row.append(self.board.grid[i][j])
            while len(temp_row) < self.board.size:
                temp_row.append(None)
            temp_row = temp_row[::-1]
            for j in range(self.board.size):
                if temp_row[j] is not None:
                    temp_row[j].set_merged_once(False)
                self.board.grid[i][j] = temp_row[j]
            

    def move_left(self):
        for i in range(self.board.size):
            temp_row = []
            for j in range(self.board.size):
                if not self.board.grid[i][j]:
                    continue
                if len(temp_row) == 0:
                    temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() == self.board.grid[i][j].get_value():
                    if not temp_row[-1].is_merged_once():
                        temp_row[-1].set_value(temp_row[-1].get_value() * 2)
                        temp_row[-1].set_merged_once(True)
                    else:
                        temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() != self.board.grid[i][j].get_value():
                    temp_row.append(self.board.grid[i][j])
            while len(temp_row) < self.board.size:
                temp_row.append(None)
            for j in range(self.board.size):
                if temp_row[j] is not None:
                    temp_row[j].set_merged_once(False)
                self.board.grid[i][j] = temp_row[j]


    def move_top(self):
        for j in range(self.board.size):
            temp_row = []
            for i in range(self.board.size):
                if not self.board.grid[i][j]:
                    continue
                if len(temp_row) == 0:
                    temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() == self.board.grid[i][j].get_value():
                    if not temp_row[-1].is_merged_once():
                        temp_row[-1].set_value(temp_row[-1].get_value() * 2)
                        temp_row[-1].set_merged_once(True)
                    else:
                        temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() != self.board.grid[i][j].get_value():
                    temp_row.append(self.board.grid[i][j])
            while len(temp_row) < self.board.size:
                temp_row.append(None)
            for i in range(self.board.size):
                if temp_row[i] is not None:
                    temp_row[i].set_merged_once(False)
                self.board.grid[i][j] = temp_row[i]

    def move_down(self):
        for j in range(self.board.size):
            temp_row = []
            for i in range(self.board.size - 1, -1, -1):
                if not self.board.grid[i][j]:
                    continue
                if len(temp_row) == 0:
                    temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() == self.board.grid[i][j].get_value():
                    if not temp_row[-1].is_merged_once():
                        temp_row[-1].set_value(temp_row[-1].get_value() * 2)
                        temp_row[-1].set_merged_once(True)
                    else:
                        temp_row.append(self.board.grid[i][j])
                elif temp_row[-1].get_value() != self.board.grid[i][j].get_value():
                    temp_row.append(self.board.grid[i][j])
            while len(temp_row) < self.board.size:
                temp_row.append(None)
            temp_row = temp_row[::-1]
            for i in range(self.board.size):
                if temp_row[i] is not None:
                    temp_row[i].set_merged_once(False)
                self.board.grid[i][j] = temp_row[i]

