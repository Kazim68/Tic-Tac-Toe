import time
from player import HumanPlayer, RandomComputerPlayer, AIcomputerPlayer


class TicTacToe:
    def __init__(self):
        # a single list to represent 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keeps track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            self.current_winner = letter if self.winner(
                square, letter) else None
            return True
        return False

    def winner(self, square, letter):
        # checking rows
        row_idx = square // 3
        row = self.board[row_idx * 3: (row_idx + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # checking columns
        col_idx = square % 3
        col = [self.board[col_idx + i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # checking diagonals
        if square % 2 == 0:  # since diagonals are [0 2 4 6 8]
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # for left to right diagonal
            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # for right to left diagonal
            if (all([spot == letter for spot in diagonal1])) or (all([spot == letter for spot in diagonal2])):
                return True

        # if all checks fail
        return False


def play(game, x_player, o_player, print_game=True):
    # return winner of game and None if tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    while game.empty_squares():

        # get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # make the move
        if game.make_move(square, letter):
            if print_game:
                print(str(square) + f' makes a move to square {square}')
                game.print_board()
                print(' ')  # prints an empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

        # alternate letters
        letter = 'X' if letter == 'O' else 'O'

        # tiny time break to make things a little bit easier to read
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie')


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = AIcomputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
