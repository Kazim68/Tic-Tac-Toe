import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter
        # letter -> O or X

        # we want players to get next move given a game
        def get_move(game):
            pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if square in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')
        return val


class AIcomputerPlayer(Player):  # using a minimax algorithm for AI bot in game
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # this selects a random square if all square are available
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first let's check if the previous move was a winner
        # this is our base case
        if state.current_winner == other_player:
            # we need to return position and score for minimax algorithm to work so we are using a dictionary
            return {'position': None, 'score': 1*(state.num_empty_squares()+1) if other_player == max_player else
                    -1*(state.num_empty_squares()+1)
                    }
        elif not state.empty_squares():  # when no empty squares
            return {'postion': None, 'score': 0}

        # initialize some dictionaries
        if player == max_player:
            # each score should be maximize (larger) so small value
            best = {'postion': None, 'score': -math.inf}
        else:
            # each score should be minimize
            best = {'postion': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # Step1: make a move, try that spot
            state.make_move(possible_move, player)
            # Step2: recurse using minimax to simulate a game after making that move
            sim_move = self.minimax(state, other_player)
            # Step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            # otherwise we will get messed up
            sim_move['position'] = possible_move
            # Step4: update dictionaries if necessary
            if player == max_player:  # maximize the max player
                if sim_move['score'] > best['score']:
                    best = sim_move  # replace best
            else:  # minimize the other player
                if sim_move['score'] < best['score']:
                    best = sim_move  # replace best
        return best
