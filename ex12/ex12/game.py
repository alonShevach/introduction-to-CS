DEFAULT_GOAL_NUM = 4
DEFAULT_ROWS_NUM = 6
DEFAULT_COLS_NUM = 7
class Game:
    def __init__(self):
        """
        the constractor of the game, having a default cols rows and goal num
        for the four in a row game.
        :param cols: number of cols in the board.
        :param rows: number of rows in the board.
        :param goal_num: the number of rings you need to get together,
        in this game 4.
        """
        self._cols = DEFAULT_COLS_NUM
        self._rows = DEFAULT_ROWS_NUM
        self._goal = DEFAULT_GOAL_NUM
        self._player1_rings = []
        self._player2_rings = []
        self._arena = [[0 for i in range(self._cols)] for j
                       in range(self._rows)]
        self._current_player = 1

    def __repr__(self):
        txt = ''
        for i in range(0, len(self._arena)):
            for j in range(len(self._arena[i])):
                txt += str(self._arena[i][j])
            txt += '\n'
        return txt
    def get_board(self):
        return self._arena
    def get_player_at(self, row, col):
        """
        a function that return the player a current spot on the board.
        :param row: row for the player to be in
        :param col: col for the player to be in
        :return: the player in the spot.
        """
        if(row>self._rows-1 or col>self._cols-1 or row<0 or col<0):
            raise Exception("illegal location in : get Player at")
        return self._arena[row][col] if self._arena[row][col] else None

    def spot_content(self, spot):
        """
        a function that returns the spot content of a given spot.
        :param spot: a spot to see what there is in.
        :return: the number of the player in the spot,
        if there is no player there, return None.
        """
        if spot in self._player1_rings:
            return 1
        elif spot in self._player2_rings:
            return 2
        else:
            return None

    def get_winner(self):
        """
        a function that returns the winner of the game if there is a winner,
        if the board is full returns 0
        if the game did not finish yet returns None.
        """
        for i in [1, 2]:
            if self.check_if_player_won(i):
                return i
            if self.is_board_full():
                return 0
        return None

    def is_possible_move(self, col):
        """
        a function that checks if there are places left on a
        given column
        :param col: a column to see if there is available place in.
        :return: True if the move is possible, False otherwise.
        """
        if self.spot_content([0, col]) is None:
            return True
        else:
            return False

    def make_move(self, column):
        """
        a function that does a move on the game board.
        :param column: a column to do the move in.
        :return: a tuple with the position that the ring has
        added to upon success.
        False otherwise.
        """
        if self.get_winner() is not None or column>self._cols-1 \
                or column<0 or self.spot_content((0,column)):
            raise Exception("Illegal Move")
        player_num = self.get_current_player()
        if player_num == 1:
            rings = self._player1_rings
            self._current_player = 2
        else:
            rings = self._player2_rings
            self._current_player = 1
        for i in range(self._rows - 1, -1, -1):
            if self.spot_content([i, column]) is None:
                rings.append([i, column])
                self._arena[i][column] = player_num
                return (i, column)
        return False

    def get_current_player(self):
        """
        a function that return the current player playing.
        """
        return self._current_player

    def is_board_empty(self):
        """
        a function that checks if the game board is empty.
        :return: True if empty, False otherwise
        """
        if not self._player1_rings and not self._player2_rings:
            return True
        return False

    def is_board_full(self):
        """
        a function that checks if the game board is full
        :return: True if full, False otherwise
        """
        for col in range(self._cols):
            if self.is_possible_move(col):
                return False
        return True

    def check_if_player_won(self, player_num):
        """
        a function that checks if a given player has won the game.
        getting the player's num.
        :param player_num: the number of the player we wish to check if he won.
        :return: True if the player did won, False otherwise.
        """
        if player_num == 1:
            rings = self._player1_rings
        else:
            rings = self._player2_rings
        rings.sort()
        # counting if we have four in a row.
        for row, col in rings:
            diag_count = 0
            row_count = 0
            col_count = 0
            up_diag_count = 0
            for i in range(self._goal):
                if [row + i, col] in rings:
                    row_count += 1
                if [row, col + i] in rings:
                    col_count += 1
                if [row + i, col + i] in rings:
                    diag_count += 1
                if [row - i, col + i] in rings:
                    up_diag_count += 1
            if (diag_count == self._goal) or (col_count == self._goal)\
                    or (row_count == self._goal) or (
                    up_diag_count == self._goal):
                return True
        return False
