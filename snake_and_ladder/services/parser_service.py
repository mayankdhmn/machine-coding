from typing import cast
from models.snake import Snake
from models.ladder import Ladder
from models.player import Player 
from models.dice import Dice


class Parser: 
    """
    



    """
    def parse_input_file(self, input_file):
        """

        Returns 
            tuple{int} -- (list_of_ladders, players, snakes, dice}
        """
        try:
            with open(input_file, 'r') as f:
                dies = []
                snakes = []
                ladders = []
                players = [] 

                board_size = int(f.readline().strip())

                die_count = int(f.readline().strip())
                die_size = int(f.readline().strip())

                snake_count = int(f.readline().strip())
                for _ in range(snake_count):
                    start, end = map(int, f.readline().strip().split())
                    snakes.append(Snake(start, end))
                
                ladder_count = int(f.readline().strip())
                for _ in range(ladder_count):
                    start, end = map(int, f.readline().strip().split())
                    ladders.append(Ladder(start, end))

                player_count = int(f.readline().strip())
                for _ in range(player_count):
                    player_name = f.readline().strip()
                    players.append(Player(player_name))

                return (die_count, die_size, board_size, snakes, ladders, players)
        except FileNotFoundError:
            print('File with name ' + input_file + ' not found.')
        except:
            print('Some exception occured')
