###################################################################
# FILE : board.py                                                 #
# EXERCISE : intro2cs1 ex9 2018-2019                              #
# DESCRIPTION: a file for class board, for board in rush hour game#
###################################################################

MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"
DEFAULT_TARGET_LOCATION = (3, 7)
DEFAULT_BOARD_SIZE = 7

class Board:
    """
    The purpose of this class is to make a board for a game with cars in the board,
    the cars should be in Car type class, and this board is the game board where
    the cars are on.
    """

    def __init__(self, target_location=DEFAULT_TARGET_LOCATION, board_size=DEFAULT_BOARD_SIZE):
        """
        the constructor of the class
        :param target_location: a target that is the car's target destination.
        :param board_size:
        """
        self.__size = board_size
        self.__target_location = target_location
        self.__car_dict = {}
        self.__possible_moves_lst = self.possible_moves()
        self.__board_cells = self.cell_list()
        self.__game_board = self.make_board()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        string_to_print = []
        # to print the line if the target's location is on the bottom,
        # or on the top of the board.
        target_line = (['*']*self.__target_location[1]) + \
                      [self.__game_board[-1][0]] + ['*']* \
                      (self.__size-self.__target_location[1]-1)
        # if the target's location in the beginning of the board.
        if self.__target_location[0] < 0:
            string_to_print.append(str(target_line))
        for index, line in enumerate(self.__game_board):
            # if the index is on the end of the board, and
            # if the target location is on the bottom of the board.
            if self.__target_location[0] == self.__size and self.__target_location[0] == index:
                string_to_print.append(str(target_line))
                break
            # if we reached the end of the board, we already
            # printed the target's location.
            if index == len(self.__game_board) - 1:
                break
            # if it is on the target's location line, prints the target
            # location as well
            if index == self.__target_location[0] and self.__target_location[0] != self.__size:
                # if the target location is in the beginning of the board.
                if self.__target_location[1] > 0:
                    string_to_print.append(str(line) + str(self.__game_board[-1]))
                else:
                    string_to_print.append(str(self.__game_board[-1]) + str(line))
                continue
            if self.__target_location[1] < 0:
                string_to_print.append(str(['*']) + str(line))
            else:
                string_to_print.append(str(line))
        # prints each line separately.
        return '\n'.join(string_to_print)

    def make_board(self):
        """
        a function that creates the board and updates it to out needs,
        moving the cars.
        uses the cell_content function
        :return: the game board with the current location of everything.
        """
        updated_board = []
        temporary_lst = []
        # runs on the board cells, and for any empty cell adds '_'
        # for cells with car in it puts the car's name
        for index, cell in enumerate(self.__board_cells):
            if index % self.__size == 0 and index != 0:
                updated_board.append(temporary_lst)
                temporary_lst = []
            content = self.cell_content(cell)
            # if the cell is empty
            if content is None:
                temporary_lst.append('_')
            else:
                # if not, adds the car name
                temporary_lst.append(content)
        updated_board.append(temporary_lst)
        return updated_board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_list = []
        for i in range(self.__size):
            for j in range(self.__size):
                cell_list.append((i, j))
        cell_list.append(self.target_location())
        return cell_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        using Car.possible_moves() and Car.movement_requirements.
        :return: list of tuples of the form (name, movekey, description)
                 representing legal moves
        """
        list_of_possible_moves = []
        for car, (car_name, coordinates) in self.__car_dict.items():
            # this for loop runs maximum twice on our game.
            for key in car.possible_moves():
                # Note that the last for loop, runs for 1 object, but if we
                # will play another game we might want it to be more,
                # so i created a loop.
                for move in car.movement_requirements(key):
                    if self.cell_content(move) is None or move == self.__target_location:
                        list_of_possible_moves.append((car_name, key, 'you can move to the direction'+ key))
        return list_of_possible_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return self.__target_location

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty, and False if coordinate not
        in the board.
        """
        # implement your code and erase the "pass"
        if coordinate not in self.__board_cells:
            return False
        for car, (car_name, coordinate_lst) in self.__car_dict.items():
            for coordinate1 in coordinate_lst:
                # if the coordinate given is in the car_lst
                # returns the car name.
                if coordinate == coordinate1:
                    return car_name
        # if there is no car in the current location.
        return None

    def add_car(self, car):
        """
        Adds a car to the game board.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for coordinate in car.car_coordinates():
            if self.cell_content(coordinate) is not None:
                return False
        car_name = car.get_name()
        self.__car_dict[car] = (car_name, car.car_coordinates())
        # updates game board.
        self.__game_board = self.make_board()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # if the car can't move to this direction.
        if (name, movekey, 'you can move to the direction'+ movekey) not in self.possible_moves():
            return False
        for car, (car_name, coordinates) in self.__car_dict.items():
            if car_name == name:
                # moves the car according to the given direction.
                if not car.move(movekey):
                    return False
                self.__car_dict[car] = (car_name, car.car_coordinates())
                break
        # updates game board.
        self.__game_board = self.make_board()
        # updates the possible moves, according to the new car.
        self.__possible_moves_lst = self.possible_moves()
        return True
