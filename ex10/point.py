class Point:
    """
    The following represents a Point
    on a 2 Dimensional space.
    """
    def __init__(self,y_cor,x_cor):
        """
        The following creates a new point,
        :param y_cor: a given Y cpordinate (can be a float)
        :param x_cor:  a given X coordinate (can be a float)
        """
        self._x_cor=x_cor
        self._y_cor=y_cor
    def get_x(self):
        """
        The following returns point's x-coor
        :return: current point x-coordinate
        """
        return self._x_cor
    def get_y(self):
        """
        The following returns point's y coordinate.
        :return: current Point's y-cor
        """
        return self._y_cor
    def set_x(self,x):
        """
        The following sets point's x_cor
        :param x:  a given number
        :return: None
        """
        self._x_cor=x
    def set_y(self,y):
        """
        The following sets point's y-cor
        :param y: a given number
        :return: None
        """
        self._y_cor=y