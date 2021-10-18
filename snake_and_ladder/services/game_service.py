from collections import deque

class SnakeAndLadder:
    def __init__(self, board, players, dice_service):
        self.board = board
        self.players = players
        self.dice_service = dice_service

        self.players_loc, self.player_id_vs_name, self.cons_chance, self.cons_roll_sum = {}, {}, 0, 0
        for player in players:
            self.players_loc[player.get_id()] = 0
            self.player_id_vs_name[player.get_id()] = player.get_name()
            
    def play(self):
        with open('output_file.txt', 'w') as f:
            active_players = deque()
            for player in self.players:
                active_players.append(player.get_id())
            while len(active_players) > 0:
                curr_player = active_players.popleft()
                curr_roll = self.dice_service.roll()
                prev = self.players_loc[curr_player]
                if (curr_roll == self.dice_service.dice.get_size() * self.dice_service.get_num_dice()): 
                    if not self.players_loc[curr_player]:
                        print(self.player_id_vs_name[curr_player] + ' has unlocked', file=f)
                    else:
                        if self.cons_chance < 2:
                            print(self.player_id_vs_name[curr_player] + ' has got another chance!!!!!', file=f)
                            self.cons_chance = self.cons_chance + 1
                            self.cons_roll_sum = self.cons_roll_sum + curr_roll
                            active_players.appendleft(curr_player)
                            continue
                        else:
                            print(self.player_id_vs_name[curr_player] + ' has lost his chances!!!', file=f)
                            self.cons_roll_sum = 0
                if self.players_loc[curr_player] + curr_roll + self.cons_roll_sum > self.board.get_size():
                    active_players.append(curr_player)
                    self.cons_roll_sum = 0
                    self.cons_chance = 0
                    continue
                self.players_loc[curr_player] = self.players_loc[curr_player] + curr_roll + self.cons_roll_sum
                self.cons_roll_sum = 0
                self.cons_chance = 0
                if self.players_loc[curr_player] in self.board.snake_mapping:
                    self.players_loc[curr_player] = self.board.snake_mapping[self.players_loc[curr_player]]
                if self.players_loc[curr_player] in self.board.ladder_mapping:
                    self.players_loc[curr_player] = self.board.ladder_mapping[self.players_loc[curr_player]]
                print(self.player_id_vs_name[curr_player] + ' rolled a ' + str(curr_roll) + 'and moved from ' + str(prev) + ' to ' + str(self.players_loc[curr_player]), file=f)
                if self.players_loc[curr_player] == self.board.get_size():
                    print(self.player_id_vs_name[curr_player] + ' wins the game', file=f)
                    continue
                active_players.append(curr_player)
        