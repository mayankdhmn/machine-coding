from services.game_service import Game
from models.board import Board

def main():
    board = Board()
    game = Game(board)
    game.play()

if __name__ == '__main__':
    main()