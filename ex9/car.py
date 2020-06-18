#################################################################
# FILE : car.py                                                 #
# WRITER : alon shevach , alon.shevach , 20595420               #
# EXERCISE : intro2cs1 ex9 2018-2019                            #
# DESCRIPTION: a file for class car, for cars in rush hour game #
#################################################################

VERTICAL = 0
HORIZONAL = 1
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"

class Car:
    """
    This class is for cars, the cars are able to move 1 step to each direction(up,
    down, left, right) each car has a name, length, location and orientation. a car can only
    move in the direction of the orientation.
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: The car way of movement.
        """
        self.__name = name
        self.__length = length
        self.location = location
        self.__orientation = orientation
        self.__coordinates = self.car_coordinates()

    def car_coordinates(self):
        """
        makes coordinates for a given car, making it with the car's orientation,
        and the car length.
        :return: A list of coordinates the car is in
        """
        coordinates = []
        if self.__orientation == HORIZONAL:
            for i in range(self.__length):
                coordinates.append((self.location[0], self.location[1]+i))
        elif self.__orientation == VERTICAL:
            for i in range(self.__length):
                coordinates.append((self.location[0]+i, self.location[1]))
        return coordinates

    def possible_moves(self):
        """
        This function returns a dict of the possible moves of this car
        For this car type, keys are from 'udrl'
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.__orientation == HORIZONAL:
            results = {'r':  "you can move right", 'l': 'you can move left'}
        elif self.__orientation == VERTICAL:
            results = {'u': 'you can move up', 'd': 'you can move down'}
        else:
            return {}
        return results

    def movement_requirements(self, movekey):
        """
        This function gives the car movement requirements according to the car's movekey given.
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        moves_require_lst = []
        # updates the list according to the possible moves.
        if self.__orientation == HORIZONAL:
            if movekey == MOVE_RIGHT:
                moves_require_lst.append((self.__coordinates[0][0], self.__coordinates[-1][1] + 1))
            elif movekey == MOVE_LEFT:
                moves_require_lst.append((self.__coordinates[0][0], self.__coordinates[0][1] - 1))
        elif self.__orientation == VERTICAL:
            if movekey == MOVE_UP:
                moves_require_lst.append((self.__coordinates[0][0] - 1, self.__coordinates[0][1]))
            elif movekey == MOVE_DOWN:
                moves_require_lst.append((self.__coordinates[-1][0] + 1, self.__coordinates[0][1]))
        return moves_require_lst

    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.__orientation == VERTICAL:
            if movekey == MOVE_UP:
                self.location = (self.location[0] - 1, self.location[1])
            elif movekey == MOVE_DOWN:
                self.location = (self.location[0] + 1, self.location[1])
            else:
                # if orientation does not fit the move keys
                return False
        elif self.__orientation == 1:
            if movekey == MOVE_LEFT:
                self.location = (self.location[0], self.location[1] - 1)
            elif movekey == MOVE_RIGHT:
                self.location = (self.location[0], self.location[1] + 1)
            else:
                # if orientation does not fit the move keys
                return False
        else:
            return False
        # Update the coordinates.
        self.__coordinates = self.car_coordinates()
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
