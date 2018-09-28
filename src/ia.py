import utils
import math
import numpy as np


class IA:
    def __init__(self):
        pass

    def next_move(self, board) -> tuple:
        _, best_movement = self._minimax(board)
        print(best_movement)
        return best_movement

    def _minimax(self, board, alfa=-math.inf,
                 beta=math.inf, current_player='G', max_level=4):

        best_movement = ()

        if max_level == 0:
            return (self._heuristics(board), ())

        if current_player == 'G':
            value = -math.inf
            for movement in utils.all_possible_moves(board):
                next_board = np.copy(board)
                next_board[movement] = 'G'

                _minimax, _ = self._minimax(next_board, alfa, beta,
                                            current_player='X',
                                            max_level=max_level - 1)

                if _minimax > value:
                    value = _minimax
                    best_movement = movement

                alfa = max(value, alfa)

                if beta <= alfa:
                    break

        else:
            value = math.inf
            for movement in utils.all_possible_moves(board):
                next_board = np.copy(board)

                next_board[movement] = current_player
                minimax, _ = self._minimax(next_board, beta, alfa,
                                           current_player='G',
                                           max_level=max_level - 1)
                if minimax < value:
                    value = minimax
                    best_movement = movement

                beta = min(value, beta)

                if beta <= alfa:
                    break

        return value, best_movement

    def _heuristics(self, board):
        postive_factor = 10 * (utils.find_doublets('G', board) +
                               100 * (utils.find_triplets('G', board) +
                                      1000 * utils.find_quartets('G', board)))
        negative_factor = 10 * (utils.find_doublets('X', board) +
                                100 * (utils.find_triplets('X', board) +
                                       1000 * utils.find_quartets('X', board)))

        return postive_factor - 0.5 * negative_factor
