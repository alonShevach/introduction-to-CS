######################################################################
# FILE : game.py                                                     #
# EXERCISE : intro2cs1 ex9 2018-2019                                 #
# DESCRIPTION: a file for class game for rush hour game, also runs   #
# the rush hour game, with default settings and with json file given #
######################################################################


from board import Board
from car import Car
import helper
import sys

POSSIBLE_MOVES = 'udlr'
ALLOWED_CARS = 'YBOWGR'
VERTICAL = 0
HORIZONAL = 1


class Game:
    """
    a class that runs the rush hour game, using the classes Car and Board,
    the game finishes when a car arrive to the target location according to the board.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        :param dict_of_cars: dict of cars on the given board, with a car type and his name.
        """
        self.board = board
        self.board_cell_lst = board.cell_list()
        self.__target_location = board.target_location()

    def ask_input_and_check_input(self):
        """
        a function that checks if the user's input is ok according to the
        instructions of the game. and if the car is on the board.
        :return: a tuple of the car type and input(car_name, direction) if the input
        is ok, if not, returns False
        """
        user_input = input('please write down the color of the car you '
                           'wish to move, and the direction: ')
        if len(user_input) != 3 or user_input[1] != ',':
            print('Bad input length or no "," between car and direction.')
            return False
        car, direction = user_input.split(',')
        # Checks if the cars and direction fits the instructions.
        if car not in ALLOWED_CARS:
            print('bad car color')
            return False
        if direction not in POSSIBLE_MOVES:
            print("bad direction")
            return False
        return car, direction

    def __single_turn(self):
        """
        a method that runs a single turn on rush hour,
        asking for a user's input, checks if it is valid.
        then apply the move to the game board
        :return: True success move, False failed moving.
        """
        input_value = self.ask_input_and_check_input()
        # if it returned False
        if not input_value:
            return False
        # unpack the tuple if the input is ok.
        car_name, direction = input_value
        for new_car_name, new_direction, disc in self.board.possible_moves():
            # finding the right car.
            if new_car_name != car_name:
                continue
            # if the direction is in the dictonary of possible moves, and it is the input.
            if direction == new_direction:
                self.board.move_car(car_name, direction)
                return True
        print("cannot move to that direction, the space is not empty or you reach the "
              "end of the board")
        return False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # as long as the target location is empty, continue playing.
        while self.board.cell_content(self.__target_location) is None:
            if self.__single_turn():
                # when moved successfully it prints the board.
                print(self.board)
            else:
                continue
        # if got out of the while loop, meaning you won.
        print('YOU WON!!!')


def add_cars_to_board(valid_cars, board):
    """
    a function that adds the valid cars to the game board
    :param valid_cars: valid cars from the json file, after checking they
    follow the instructions
    :param board: the current board to add the cars to
    :return: the game board after adding the cars, and dictonary with the cars added,
    the keys are the car names and the value is the car type obj.
    """
    for key, value in valid_cars.items():
        new_car = Car(key, value[0], value[1], value[2])
        board.add_car(new_car)
    return board


def check_json_file(file_output, board):
    """
    a function that checks whether each car in the json file follow
    the instructions of the game, if not, removes it.
    :param file_output: the output of the json file.
    :param board: the board of the current game.
    :return: a new dictonary, without the cars that does not follow the instructions.
    """
    target_location = board.target_location()
    board_size = int(len(board.cell_list())**0.5)
    dict_of_valid_cars = {}
    for key, (length, location, orientation) in file_output.items():
        # If the orientation is valid.
        if orientation != HORIZONAL and orientation != VERTICAL:
            continue
        # if the length is bigger than the board size, if wont fit the board.
        if length > board_size:
            continue
        if location[0] > board_size or location[0] < 0 or\
                location[1] > board_size or location[1] < 0:
            continue
        # if the car size with its location will be out of the board.
        if orientation == 1 and (((length + location[1]-1) >= board_size) and
                                 location[0] != target_location[0]):
            continue
        if orientation == 0 and ((length + location[0]-1) >= board_size):
            continue
        dict_of_valid_cars[key] = (length, location, orientation)
    return dict_of_valid_cars


if __name__ == "__main__":
    # creates a board for the game
    game_board = Board()
    # Load json file
    json_file_output = helper.load_json(sys.argv[1])
    # check for the valid cars in json file.
    valid_json_file_cars = check_json_file(json_file_output, game_board)
    game_board = add_cars_to_board(valid_json_file_cars, game_board)
    # starts the game
    print(game_board)
    run_game = Game(game_board)
    run_game.play()

