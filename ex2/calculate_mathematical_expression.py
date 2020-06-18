def calculate_mathematical_expression(num1, num2, exp):
    """calculates a mathematical expression, by getting 3 parameters, 2 numbers (num1, num2) and a math sign(exp = +,-,*,/)"""
    if exp == '+':
        return (num1+num2)
    elif exp == '*':
        return (num1*num2)
    elif exp == '-':
        return (num1-num2)
    elif num2 == 0:
        return None
    elif exp == '/':
        num1 = float(num1)
        num2 = float(num2)
        return (num1/num2)
    else:
        return None
def calculate_from_string(mathstring):
    """calculates a mathematical expression, by getting only 1 string which contains 2 numbers and a math sign divided by spaces. using another function"""
    new_num1, new_exp, new_num2 = mathstring.split()
    new_num1 = int(new_num1)
    new_num2 = int(new_num2)
    return calculate_mathematical_expression(new_num1, new_num2, new_exp)