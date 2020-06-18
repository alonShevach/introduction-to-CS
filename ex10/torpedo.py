TORPEDO_RADIUS = 4
class Torpedo:
    """
    The following represents a torpedo object,
    which has-
    position
    speed
    direction
    """
    def __init__(self,position,speed,direction):
        """
        The following produces a new torpedo object
        :param position: 2D point
        :param speed: speed2D object
        :param direction: heading (integer\float)
        """
        self._position=position
        self._speed=speed
        self._dirction=direction
    def get_speed(self):
        """
        The following returns this object's speed
        :return: self.speed (Speed2D)
        """
        return self._speed
    def get_position(self):
        """
        The following returns this torpedo's
        position
        :return: self.position  (Point2D)
        """
        return self._position
    def get_direction(self):
        """
        The following returns current object's
        direction (integer\float)
        :return: Torpedo's heading
        """
        return self._dirction
    def set_position(self,new_position):
        """
        The following sets the following object Position
        :param new_position: Point2D
        :return: None
        """
        self._position=new_position
    def get_radius(self):
        """
        The following returns current torpedo's radius (integer\float)
        :return: Torpedo's radius
        """
        return TORPEDO_RADIUS