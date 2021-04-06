#############################################################
# FILE : math_print.py
# EXERCISE : intro2cs1 ex1 2018-2019
# DESCRIPTION: A program that prints an answer to some math questions.
#############################################################
import math
def golden_ratio():
    """function giving the golden ratio"""
    print((1+(math.sqrt(5)))/2)
def six_cubed():
    """function that gives the solution to 6 in power 3"""
    print(math.pow(6, 3))
def hypotenuse():
    """calculating the hypotenuse of a triangle with perpendicular 3 and 5 by pythagoras theorem"""
    print(math.sqrt(math.pow(3, 2)+math.pow(5, 2)))
def pi():
    """function for printing pi"""
    print(math.pi)
def e():
    """function printing e the mathematical constant"""
    print(math.e)
def triangular_area():
    """function that gives the area of triangles with different sides by the sentence
    triangle area is base*height/2"""
    print((1*1)/2, (2*2)/2, (3*3)/2, (4*4)/2, (5*5)/2, (6*6)/2, (7*7)/2, (8*8)/2, (9*9)/2, (10*10)/2)

if __name__ == "__main__" :
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()

