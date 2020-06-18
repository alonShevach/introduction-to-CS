import random

DEFAULT_COMP_PLAYER = 2


class AI:

    def __init__(self, game, player=DEFAULT_COMP_PLAYER):
        """
        the constractor of the ai class.
        :param game: a game type game.
        :param player: number of player we wish to be the ai.
        """
        self._player = player
        self._game = game
        self._last_move = 0

    def set_game(self, new_game):
        """
        a function we use to set the game to a new game,
        used if the player wants another game.
        :param new_game: a game type.
        """
        self._game = new_game

    def get_player(self):
        """
        a function that returns the ai player's num
        """
        return self._player
    def find_legal_move(self,timeout=None):
        """
        a function that finds a legal move for the computer player, using the game.
        :return: the column of the legal move.
        """
        if self._game.get_winner() is not None:
            return None
        col = random.randint(0, 6)
        cols=set()
        while not self._game.is_possible_move(col):
            col = random.randint(0, 6)
            cols.add(col)
            for i in range(7):
                    if i not in cols:
                        break
            else:
                raise Exception("No possible AI moves")
        self._last_move = col
        cols.add(col)
        return col

    def get_last_found_move(self):
        """
        a function that returns the last move from this ai.
        """
        return self._last_move
