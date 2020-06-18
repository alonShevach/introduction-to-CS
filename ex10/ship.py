RADIUS_OF_SHIP = 1


class Ship:
    """
    The following represents the ship object,
    which has - position, speed,direction and life.
    """
    def __init__(self,point,speed,direction,life=3):
        """
        The following makes a new ship object
        :param point: a given Point object .
        :param speed:  a given Speed2D object .
        :param direction: a given heading - angle of the ship.
        :param life: life, default is 3
        """
        self._position=point
        self._speed=speed
        self._direction=direction
        self._life=life

    def get_speed(self):
        """
        The following returns Speed2D obj,
        the speed of current ship.
        :return: ship's speed (Speed2D object)
        """
        return self._speed
    def get_position(self):
        """
        The following returns a Point obj -
        which is the position of the current ship.
        :return: ship's position
        """
        return self._position
    def get_direction(self):
        """
        The following returns the heading of the
        current chip.
        :return: ship's heading.
        """
        return self._direction
    def set_position(self,new_position):
        """
        The following takes a Point object,
        and sets the current ship's position to be
        that point.
        :param new_position: Point2D object
        :return:None
        """
        self._position=new_position
    def change_direction(self, new_direction):
        """
        The following takes an integer, and set's
        ship's heading to be that number*7.
        :param new_direction: integer / either float.
        :return:None
        """
        self._direction+=new_direction*7
    def set_speed(self,newSpeed):
        """
        The following takes Speed2D obj, and
        sets this ship's speed to that speed
        :param newSpeed: Speed2D object
        :return:None
        """
        self._speed=newSpeed
    def get_radius(self):
        """
        The following return's Ship's radius
        :return: Ship's radius
        """
        return RADIUS_OF_SHIP
    def get_life(self):
        """
        The following return's ship life
        :return: ship's life
        """
        return self._life
    def decrease_ship_health(self,deduce_fact=1):
        """
        The following decreases ship's life in 1
        :param :deduce_fact - how much life to decrease
        :return: None.
        """
        self._life -= deduce_fact

