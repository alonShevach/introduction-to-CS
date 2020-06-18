class Speed2D:
    """
    The following represents a speed on a 2 dimensional space
    """
    def __init__(self, y_axis_speed, x_axis_speed):
        """
        The following creates a new speed object
        :param y_axis_speed: a given number
        :param x_axis_speed: a given number
        """
        self._x_speed=x_axis_speed
        self._y_speed=y_axis_speed
    def get_x_speed(self):
        """
        The following returns the following x_axis speed factor
        :param self: self
        :return: x_speed
        """
        return self._x_speed
    def get_y_speed(self):
        """
        The following returns the following y_axis factor
        :param self: self
        :return: y_speed
        """
        return self._y_speed
    def set_x_speed(self,x):
        """
        The following sets current object x_axis_speed
        to x
        :param self: this
        :param x: a given number
        :return:None
        """
        self._x_speed=x
    def set_y_speed(self,y):
        """
        The following sets current object y_axis_speed
        :param self: this
        :param y:a given number
        :return: None
        """
        self.get_y_speed=y