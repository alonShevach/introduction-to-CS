import math


def calculate_circle_area():
    """function that gets input for user's circle's radius, and gives the area of that circle"""
    radius = float(input(''))
    circle_area = math.pi*(radius**2)
    return circle_area


def calculate_rectangle_area():
    """function that gets input for the user's rectangle sides, and gives the area of that rectangle"""
    side1 = float(input(""))
    side2 = float(input(""))
    rectangle_area = side1*side2
    return rectangle_area


def calculate_triangle_area():
    """function that gets input for the user's side of an equal sides triangle, and gives the area of that triangle"""
    triangle_side = float(input(''))
    triangle_area = ((3**0.5)/4)*(triangle_side**2)
    return triangle_area


def shape_area():
    """function that asks for user's type of shape, then uses other functions
     to calculates that shape area, and prints it to the user."""
    shape_type = input('Choose shape (1=circle, 2=rectangle, 3=triangle): ')
    if (shape_type != '1') and (shape_type != '2') and (shape_type != '3'):
        return None
    elif shape_type == '1':
        return calculate_circle_area()
    elif shape_type == '2':
        return calculate_rectangle_area()
    return calculate_triangle_area()
