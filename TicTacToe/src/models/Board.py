from pprint import pprint


class Board:
    def __init__(self, size=3):
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def __str__(self):
        pprint(self.board)
