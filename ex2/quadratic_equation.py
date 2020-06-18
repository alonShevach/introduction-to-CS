def quadratic_equation(a, b, c):
    """a function calculating the results of a quadratic equation, by getting 3 numbers, the multipliers of x**2(a),
    x(b), and the free number(c)"""
    inside_square_root = ((b**2)-4*a*c)
    if inside_square_root < 0:
        return None, None
    answer1 = (((-b)+(inside_square_root**0.5))/(2*a))
    answer2 = (((-b)-(inside_square_root**0.5))/(2*a))
    if answer1 == answer2:
        return answer1, None
    return answer1, answer2


def quadratic_equation_user_input():
    """prints the answers of the quadratic function to a user, using input for his equation"""
    user_input = input('Insert coefficients a, b, and c: ')
    if user_input == '':
        return None
    a, b, c = user_input.split()
    a = float(a)
    b = float(b)
    c = float(c)
    user_answer1, user_answer2 = quadratic_equation(a, b, c)
    if (user_answer1 == None) and (user_answer2 == None):
        return print('The equation has no solutions')
    elif user_answer1 == None:
        return print('The equation has 1 solution:', user_answer2)
    elif user_answer2 == None:
        return print('The equation has 1 solution:', user_answer1)
    return print('The equation has 2 solutions:', user_answer1, 'and', user_answer2)
