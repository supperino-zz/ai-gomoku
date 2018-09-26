import numpy
import os

QUANTITY = {
    'DUPLAS': 2,
    'TRIPLAS': 3,
    'QUADRUPLAS': 4
}


def all_possible_moves(board, player='G') -> list:
    rows, cols = numpy.where(board == '.')
    return list(zip(rows, cols))


def search(self, number=2, player='G'):
    if number is QUANTITY.DUPLAS:
        return _search_duplas(player)


def _search_duplas(self, player):
    return player


def _search_triplas(self, player):
    return 2


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
