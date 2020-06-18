def largest_and_smallest(num1, num2, num3):
    """a function giving the biggest and smallest number from 3 numbers given"""
    if num1 >= num2:
        if num2 >= num3:
            return num1, num3
        elif num3 >= num1:
            return num3, num2
        return num1, num2
    if num1 >= num3:
        return num2, num3
    elif num3 >= num2:
        return num3, num1
    return num2, num1