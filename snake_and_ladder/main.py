from models.board import Board
from models.dice import Dice
from services.parser_service import Parser
from services.dice_service import DiceService
from services.game_service import SnakeAndLadder 

def main():
    parser = Parser()
    die_count, die_size, board_size, snakes, ladders, players  =  parser.parse_input_file('inputs/input.txt')
    board = Board(board_size, snakes, ladders)
    die_service = DiceService(Dice(die_size), die_count)
    snakes_and_ladders = SnakeAndLadder(board, players, die_service)
    snakes_and_ladders.play()

if __name__ == '__main__':
    main()
