import utils
import random


class IA:
    def __init__(self):
        pass

    def next_move(self, board):
        _possible_moves = utils.all_possible_moves(board)
        return _possible_moves[random.randint(0, len(_possible_moves))]

    def _minimax(self):

        pass

    def _heuristics(self):
        pass

        """
        Procurar por todas as jogadas possíveis,
        Calcular a heuristica:= (triplas, quadr (da ia) - o mesmo do jogador)
        """
