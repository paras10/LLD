from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_type(self):
        return self.symbol

    def __str__(self):
        return self.symbol