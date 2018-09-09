class Board:
    def __init__(self):
        self.pieces = [['_' for _ in range(15)] for _ in range(15)]

    def __str__(self):
        return self.board_render(self.pieces)

    def mark_piece(self, player, x, y):
        if self.pieces[x][y] == '_':
            self.pieces[x][y] = player
            return True
        else:
            return False

    def board_render(self, pieces):
        board = ' '
        for index, row in enumerate(pieces):
            if index < 10:
                board = '{board} \n {index}   {row}'.format(
                    board=board, index=index, row='  '.join(str(e) for e in row)
                )
            else:
                board = '{board} \n {index}  {row}'.format(
                    board=board, index=index, row='  '.join(str(e) for e in row)
                )
        board = '{board}\n   '.format(board=board)
        for i in range(len(self.pieces)):
            if(i < 10):
                board = '{board}  {i}'.format(board=board, i=i)
            else:
                board = '{board} {i}'.format(board=board, i=i)
        return board


class Gomoku:
    def __init__(self):
        self.board = Board()
        self.winner = None
        self.players = {
            0: 'X',
            1: 'O'
        }
        self.current_player = 0

    def run_game(self):
        while not self.winner:
            print(self.board)
            if not self.player_move():
                print('Position already used!')
                continue
            self.check_win()
            self.toggle_player()

    def check_win(self):
        pass

    def player_move(self):
        try:
            lin_play = input('linha > ')
            col_play = input('coluna > ')
            return self.board.mark_piece('X', int(lin_play), int(col_play))

        except ValueError:
            print('Input was not a number [0..14] ')
            return False

    def toggle_player(self):
        pass


if __name__ == '__main__':
    teste = Gomoku().run_game()
