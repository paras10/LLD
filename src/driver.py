from src.models.Board import Board
from src.models.CirclePiece import CirclePiece
from src.models.CrossPiece import CrossPiece
from src.models.Player import Player
from src.services.DefaultStrategy import DefaultStrategy
from src.services.GameControlService import GameControlService
from src.utils import parse_piece


def init_game():

    while True:
        print("New game session starts")
        player1 = Player("Pravin", CrossPiece)
        player2 = Player("Chandan", CirclePiece)
        board = Board(3)
        strategy = DefaultStrategy("Simple")
        game_svc = GameControlService(board, player1, player2, strategy)

        current_player = player1
        while not game_svc.is_game_over():
            print("Enter move as x,y strictly")
            player1_move = parse_piece(input())
            game_svc.move(current_player, player1_move)
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1




if __name__ == '__main__':
    init_game()