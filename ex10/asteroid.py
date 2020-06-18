NORM_FACTOR = 5
SIZE_FACTOR = 10


class Asteroid:
    """
    The following represent an Astroid,
    which is an object with position,
    speed and size.
    """
    def __init__(self,position,speed,size):
        """
        The following creates a new Asteroid object
        :param position: A given Point2D
        :param speed: a given Speed2D
        :param size: a given integer
        """
        self._position=position
        self._speed=speed
        self._size=size
    def get_speed(self):
        """
        The following returns asteroid speed
        :return: Speed2D object (see reference)
        """
        return self._speed
    def get_position(self):
        """
        The following returns this asteroid position -
        represented by a Point2D
        :return: Point2D
        """
        return self._position
    def get_size(self):
        """
        The following returns this asteroid size
        (integer)
        :return: ship's size
        """
        return self._size
    def get_radius(self):
        """
        The following returns this asteroid normed radius
        :return: Ship's radius
        """
        return self._size * SIZE_FACTOR - NORM_FACTOR
    def set_position(self,new_position):
        """
        The following gets a point-2D
        and set's asteroid new position.
        :param new_position: A Point2D
        :return: None
        """
        self._position=new_position
    def has_intersection(self, obj):
        """
        The following takes an object which has
        a position represented by Point2D,
        and check if it intersects current asteroid.
        if true,
        :param obj: An object with get.position() that returns a point 2D
        which has get_y() and get_x() attributes.
        :return: False\True  Accordingly
        """
        obj_x, obj_y = obj.get_position().get_x(),obj.get_position().get_y()
        astroid_x, astroid_y = self._position.get_x(),self._position.get_y()
        distance = ((obj_x - astroid_x)**2 + (obj_y - astroid_y)**2)**0.5
        if distance > (self.get_radius() + obj.get_radius()):
            return False
        return True
