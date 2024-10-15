from pprint import pprint

from src.services.DefaultStrategy import DefaultStrategy


class GameControlService:
    def __init__(self, board, player1, player2, game_strategy=DefaultStrategy):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.game_strategy = game_strategy

    def move(self, player, position):
        """
        :param player:
        :param position:
        :return:
        """
        if self.board[position[0]][position[1]] is None:
            print("Already filled piece")
            raise Exception.new("Already filled piece")
        else:
            self.board[position[0]][position[1]] = player.piece
        self.game_strategy.is_win(self.board)

    def get_status(self):
        print("Is game won " + self.game_strategy.is_win(board=self.board))

    def get_current_board(self):
        pprint(self.board)

    def is_game_over(self):
        return (self.game_strategy.is_win(self.board) or
                self.game_strategy.is_tie(self.board))

    def refresh_board(self):
        pass