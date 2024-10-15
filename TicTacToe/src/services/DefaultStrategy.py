from src.services.GameStrategy import GameStrategy


class DefaultStrategy(GameStrategy):
    def __init__(self, name):
        super().__init__(name)

    def is_win(self, board):
        """
        :param board:
        :return: Boolean
        """
        return True
        pass

    def is_tie(self, board):
        pass