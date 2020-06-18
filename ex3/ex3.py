def input_list():
    """a simple function that takes inputs from the user and puts them seperated in a list"""
    string_list = []
    while True:
        string_from_user = input('')
        if string_from_user == '':
            return string_list
        string_list.append(string_from_user)


def concat_list(str_list):
    """a function that receive a list of strings and combine them to a long string with spaces between each string"""
    if not str_list:
        return ''
    connected_list = str_list[0]
    for string in range(1, len(str_list)):
        connected_list += ' ' + str_list[string]
    return connected_list


def maximum(num_list):
    """a function that gets a list of numbers and returns the biggest number"""
    if not num_list:
        return None
    biggest = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > biggest:
            biggest = num_list[i]
    return biggest


def cyclic(lst1, lst2):
    """a function that checks if the given lists are cyclic diversion of each other"""
    if len(lst1) != len(lst2):
        return False
    elif lst1 == lst2:
        return True
    for i in range(len(lst1)):
        if lst1[i] == lst2[0]:
            lst3 = lst1[i:] + lst1[:i]
            if lst3 == lst2:
                return True
    return False


def seven_boom(n):
    """a function that gets a number and gives a list of the answers according to the seven boom game"""
    boom_list = ['1']
    for i in range(2, n + 1):
        if ('7' in str(i)) or (i % 7 == 0):
            boom_list.append('boom')
        else:
            boom_list.append(str(i))
    return boom_list


def histogram(n, num_list):
    """a function that test the histogram of the list and returns it"""
    histo_listo = []
    for i in range(n):
        histo_listo.append(0)
        for j in num_list:
            if j == i:
                histo_listo[i] += 1
    return histo_listo


def prime_factors(n):
    """a function that gives the prime numbers that are the divisors of the given number, n
    the function will always find the prime factors because it goes from the smallest to the biggest numbers
    therefor it will find the prime factors 1 by 1."""
    factors = []
    divised_num = n
    divisor = 2
    # smallest prime number
    while divised_num > 1:
        if divised_num % divisor == 0:
            factors.append(divisor)
            divised_num /= divisor
        else:
            divisor += 1
    return factors


def cartesian(lst1, lst2):
    """a function that gives the cartesian multiplication of lists"""
    if (lst1 == []) or (lst2 == []):
        return []
    cartesian_lst = []
    for i in lst1:
        for j in lst2:
            cartesian_lst.append([i, j])
    return cartesian_lst


def pairs(num_list, n):
    """a function that gives a list of couples that their sum is equal to n"""
    if len(num_list) < 2:
        return []
    sums = []
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == n:
                sums.append([num_list[i], num_list[j]])
    return sums
