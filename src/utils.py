import numpy as np
import os
import regex as re
from enum import Enum


class Piece(Enum):
    EMPTY = '.'
    PLAYER = 'X'
    IA = 'G'


QUANTITY = {
    'DUPLAS': 2,
    'TRIPLAS': 3,
    'QUADRUPLAS': 4
}
WIN_REGEX = r'([X]{5})|([G]{5})'
BOARD_SIZE = 15


def _search_regex(size):
    return r'([X]{size})|([G]{size})'


def all_possible_moves(board, player=Piece.IA.value) -> list:
    rows, cols = np.where(board == Piece.EMPTY.value)
    return list(zip(rows, cols))


def search(symbol, pattern, board):
    def count_row(board, start=0):
        for row in board:
            row_string = ''.join(row)
            start += len(re.findall(r'[' + symbol + r']{' + str(pattern) + '}',
                                    row_string,
                                    overlapped=True))
        return start

    def count_diag(board, start=0):
        index = - (BOARD_SIZE + 1)
        while index < BOARD_SIZE:
            diag_string = ''.join(board.diagonal(index))
            start += len(re.findall(r'[' + symbol + r']{' + str(pattern) + '}',
                                    diag_string,
                                    overlapped=True))
            index += 1
        return start

    return (
        count_row(board) +
        count_row(np.transpose(board)) +
        count_diag(board) +
        count_diag(np.fliplr(board))
    )


def find_doublets(symbol, board):
    return search(symbol, 2, board)


def find_triplets(symbol, board):
    return search(symbol, 3, board)


def find_quartets(symbol, board):
    return search(symbol, 4, board)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
