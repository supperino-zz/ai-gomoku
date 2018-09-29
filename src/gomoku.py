import numpy as np
import utils
from utils import PIECES
import ia


class Board:
    def __init__(self):
        self._pieces = np.full((utils.BOARD_SIZE, utils.BOARD_SIZE),
                               PIECES['EMPTY'])

    def mark_piece(self, player, position):
        if self._pieces[position] == PIECES['EMPTY']:
            self._pieces[position] = player
            return True
        else:
            return False

    def __str__(self):
        return self.board_render()

    def board_render(self):
        _string_board = ''
        for index, row in enumerate(self._pieces):
            _string_board = _string_board + '  '.join(row) + '\n'
        return _string_board


class Gomoku:
    def __init__(self):
        self.board = Board()
        self.winner = None
        self.IA = ia.IA()
        self._actual_player = PIECES['PLAYER']

    def run_game(self):
        while not self.winner:
            utils.clear_screen()
            print(self.board)
            if not self.board.mark_piece(self._actual_player,
                                         self.player_move()):
                print('Position already used!')
                continue
            self.check_win()
            self.toggle_player()

    def check_win(self):
        return utils.check_row(self.board._pieces) \
            or utils.check_diagonal(self.board._pieces) \
            or utils.check_column(self.board._pieces)

    def player_move(self):
        if self._actual_player == PIECES['PLAYER']:
            try:
                return tuple(map(int, input('X, Y > ').split(',')))
            except ValueError:
                print('Input was not a number [0..14] ')
        else:
            return self.IA.next_move(self.board._pieces)

    def toggle_player(self):
        self._actual_player = PIECES['PLAYER'] \
            if self._actual_player == PIECES['IA'] else PIECES['IA']


if __name__ == '__main__':
    Gomoku().run_game()
