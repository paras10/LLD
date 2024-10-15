from abc import ABC, abstractmethod


class GameStrategy(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def is_win(self, board):
        pass

    @abstractmethod
    def is_tie(self, board):
        pass
