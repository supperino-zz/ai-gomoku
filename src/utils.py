import numpy as np
import regex as re

PIECES = {
    'EMPTY': '.',
    'PLAYER': 'X',
    'IA': 'G'
}

QUANTITY = {
    'DUPLAS': 2,
    'TRIPLAS': 3,
    'QUADRUPLAS': 4
}
WIN_REGEX = r'([X]{5})|([G]{5})'
BOARD_SIZE = 15


def _search_regex(size):
    return r'([X]{size})|([G]{size})'


def all_possible_moves(board, player=PIECES['IA']) -> list:
    rows, cols = np.where(board == PIECES['EMPTY'])
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


def check_row(pieces):
    match = None
    for row in pieces:
        row_string = ''.join(row)
        match = re.search(WIN_REGEX, row_string)
        if match:
            return match.group()[0]
    return None


def check_column(pieces):
    for column in np.transpose(pieces):
        col_string = ''.join(column)
        match = re.search(WIN_REGEX, col_string)
        if match:
            return match.group()[0]
    return None


def check_diagonal(pieces):
    index = - (BOARD_SIZE + 1)
    while index < BOARD_SIZE:
        diagonal_string = ''.join(pieces.diagonal(index))
        match = re.search(WIN_REGEX, diagonal_string)
        if match:
            return match.group()[0]
        index += 1

    index = - (BOARD_SIZE + 1)
    flipped_board = np.fliplr(pieces)
    while index < BOARD_SIZE:
        diagonal_string = ''.join(flipped_board.diagonal(index))
        match = re.search(WIN_REGEX, diagonal_string)
        if match:
            return match.group()[0]
        index += 1

    return None


def find_doublets(symbol, board):
    return search(symbol, 2, board)


def find_triplets(symbol, board):
    return search(symbol, 3, board)


def find_quartets(symbol, board):
    return search(symbol, 4, board)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
