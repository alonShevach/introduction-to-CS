#############################################################
# FILE : hello_turtle.py
# EXERCISE : intro2cs1 ex1 2018-2019
# DESCRIPTION: A program that draws 3 flowers.
#############################################################
import turtle
def intro_test():
    """This is only a test method for printing Hello"""
    print('hello')
def draw_petal():
    #drawing the flower petal
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)
def draw_flower():
    """drawing 1 flower"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)
def draw_flower_advance():
    """drawing a flower with preparation to drawing more flowers"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()
def draw_flower_bed():
    """drawing 3 flowers"""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()

if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done
    
