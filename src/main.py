import numpy as np
import regex as re
import utils

from utils import WIN_REGEX, BOARD_SIZE
from ia import IA

INITIAL_BOARD = np.full((BOARD_SIZE, BOARD_SIZE), '.')


class Gomoku:
    def __init__(self):
        self._board = np.copy(np.full((15, 15), '.'))
        self._ia = IA()
        self._winner = None
        self._players = {
            0: 'X',
            1: 'G',
        }
        self._actual_player = 0

    def run(self):
        self.render()

    def render(self):
        try:
            self._start_game()
        except ValueError:
            print('\nThe given option was not a number!')
            self.render()

    def _start_game(self, mode=1):
        while not self._winner:
            try:
                move = self._render_game(mode)
                if not self._mark_board(self._actual_player, move):
                    print('Position already in use or out of the board!')
                    continue
                self._toggle_player()
                self._winner = self._game_finished()
            except ValueError:
                print('\nOption(s) is(are) not number(s). Try again!')
                self._winner = False
        self._render_board()
        print('We have a winner')

    def _render_game(self, mode):
        self._render_board()
        if self._actual_player == 1:
            print("It is AI's turn!")
            return self._ia.next_move(self._board)
        else:
            return tuple(map(int, input('X, Y > ').split(',')))

    def _render_board(self):
        utils.clear_screen()
        for index, row in enumerate(self._board):
            print(index, end='  ') if index < 10 else print(index, end=' ')
            list(map(lambda x: print(x, end='  '), row))
            print()
        print('   ', end='')
        for i in range(len(self._board)):
            print(i, end='  ') if i < 10 else print(i, end=' ')
        print()

    def _check_row(self):
        match = None
        for row in self._board:
            row_string = ''.join(row)
            match = re.search(WIN_REGEX, row_string)
            if match:
                return match.group()[0]
        return None

    def _check_column(self):
        for column in np.transpose(self._board):
            col_string = ''.join(column)
            match = re.search(WIN_REGEX, col_string)
            if match:
                return match.group()[0]
        return None

    def _check_diagonal(self):
        index = - (BOARD_SIZE + 1)
        while index < BOARD_SIZE:
            diagonal_string = ''.join(self._board.diagonal(index))
            match = re.search(WIN_REGEX, diagonal_string)
            if match:
                return match.group()[0]
            index += 1

        index = - (BOARD_SIZE + 1)
        flipped_board = np.fliplr(self._board)
        while index < BOARD_SIZE:
            diagonal_string = ''.join(flipped_board.diagonal(index))
            match = re.search(WIN_REGEX, diagonal_string)
            if match:
                return match.group()[0]
            index += 1

        return None

    def _toggle_player(self):
        self._actual_player = 0 if self._actual_player else 1

    def _mark_board(self, player, position):
        if not self._valid_position(position) or self._board[position] != '.':
            return False
        self._board[position] = self._players[player]
        return True

    def _game_finished(self):
        return self._check_row() \
            or self._check_column() \
            or self._check_diagonal()

    def _valid_position(self, position):
        x_coord, y_coord = position
        return 0 <= x_coord <= BOARD_SIZE and 0 <= y_coord <= BOARD_SIZE


# if(__name__ == "__main__"):
#     Gomoku().run()
