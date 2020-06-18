##############################################################
# FILE : ex7.py                                              #
# WRITER : alon shevach , alon.shevach , 20595420            #
# EXERCISE : intro2cs1 ex7 2018-2019                         #
# DESCRIPTION: 10 function that have different purposes, all #
# using recursions for running the function.                 #
##############################################################

# for the 10th question only.
import copy


def print_to_n(n):
    """
    a function that prints all the numbers from 1 to a given natural number
    :param n: number to count to
    :return: returns None but prints to the user
    """
    if n < 1:
        return
    print_to_n(n-1)
    print(n)


def print_reversed(n):
    """
    a function that prints all number from a given natural number to 1.
    :param n: number to count from to 1
    :return: returns None but prints to the user
    """
    if n < 1:
        return
    print(n)
    print_reversed(n-1)


def is_prime(n):
    """
    a function that checks if number is prime, using another function
    that checks if a number has a smaller divisor.
    :param n: number to check if he is prime
    :return: True if the number is prime, False if not,
    """
    if n < 2:
        return False
    # a number's biggest divisor would be his square root.
    if has_divisor_smaller_than(n, int(n**0.5)):
        return False
    return True


def has_divisor_smaller_than(n, divisor):
    """
    a function that checks if a number has divisors smaller than a given number.
    :param n: number to check if he has divisors
    :param divisor: the number to check from, if the number divides by him, or
    by lower numbers.
    :return: True if he has smaller divisors, False if he does not.
    """
    if divisor == 1:
        return False
    # checks if the given number can be divided, also if given the same number,
    # it does not say that it is a smaller divisor, because all number divide themselves.
    if (n != divisor) and (n % divisor == 0):
        return True
    return has_divisor_smaller_than(n, divisor-1)


def exp_n_x(n, x):
    """
    a function that get 2 numbers, n, x and returns the exp sum of the numbers.
    :param n: int, bigger than 0
    :param x: float
    :return: the exp, sum of the given n and x.
    """
    if n < 0:
        return
    if n < 1:
        return 1
    return ((x ** n) / (factorial(n))) + exp_n_x(n - 1, x)


def factorial(n):
    """
    a functions to give the factorial of a number (n!)
    :param n: int bigger than 0. the number to use the factorial on.
    :return: the factorial sum of the given number.
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n - 1)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    a function that solves the hanoi game. gets the number
    of rings for the game, uses the 'hanoi' param do display the game.
    :param hanoi: this is the param that displays the game.
    :param n: number of rings in the game.
    :param src: starting point, where the rings start.
    :param dest: destination to get the rings to.
    :param temp: the empty slot, for using to move the rings.
    :return: None.
    """
    if n < 1:
        return
    if n == 1:
        hanoi.move(src, dest)
    elif n == 2:
        hanoi.move(src, temp)
        hanoi.move(src, dest)
        hanoi.move(temp, dest)
    elif n > 2:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)


def print_sequences(char_list, n):
    """
    a function that prints all the different sequences of a objects in
    list, and the length of the sequence will be a given n.
    this function  uses the 'print_sequences_helper' function.
    :param char_list: a given list of strings.
    :param n: a number, that is the length of the words to print
    :return: None, but prints to the user.
    """
    print_sequences_helper(char_list, n, '')


def print_sequences_helper(char_list, n, word):
    """
    the function that runs the 'print sequences' function.
    this function prints, and find the right words.
    :param word: the word that will be printed, after it will finish combining
    all the objects together.
    :return: None, but prints to the user.
    """
    if len(word) == n:
        print(word)
        return
    for letter in char_list:
        print_sequences_helper(char_list, n, word + letter)


def print_no_repetition_sequences(char_list, n):
    """
    a function that prints all the different sequences of a objects without
    using the same letter in the list twice.
    the length of the sequence will be a given n.
    this function  uses the 'print_no_repetition_sequences_helper' function.
    :param char_list: a given list of strings.
    :param n: a number, that is the length of the words to print
    :return: None, but prints to the user.
    """
    print_no_repetition_sequences_helper(char_list, n, '')


def print_no_repetition_sequences_helper(char_list, n, word):
    """
    the function that runs the 'print_no_repetition_sequences' function.
    this function prints, and find the right words.
    :param word: the word that will be printed, after it will finish combining
    all the objects together.
    :return: None, but prints to the user.
    """
    if len(word) == n:
        print(word)
        return
    for letter in char_list:
        if letter in word:
            continue
        print_no_repetition_sequences_helper(char_list, n, word + letter)


def parentheses(n):
    """
    a function that returns all the different ways to combine '(' and ')'
    with having the same number of '(' and ')' and the number of them is n.
    also each '(' has to be closed with ')' like in math.
    :param n: number of '(' and ')'
    :return: a list of all the different allowed combinations.
    """
    if n < 1:
        return
    parentheses_lst = []
    parentheses_helper(n, parentheses_lst, '', 0, 0)
    return parentheses_lst


def parentheses_helper(n, parentheses_lst, word, count1, count2):
    """
    a function that runs the 'parentheses' function, finds the right strings,
    and adding them to a list.
    :param word: a string that is added to the list when to function
    finishes to make it according to the explanations.
    :param count1: counts the number of time '(' appeared.
    :param count2: counts the number of time ')' appeared.
    :return: None, but changes the given list.
    """
    # if count if more than the maximum of times each one should appear.
    if count1 == n+1 or count2 == n+1:
        return
    # if the word is in the right length
    if len(word) == n*2:
        parentheses_lst.append(word)
        return
    parentheses_helper(n, parentheses_lst, word + '(', count1 + 1, count2)
    # not allowed to have a more ')' than '(' because it will make
    # 1 of the ')' to close nothing (not '(')
    if count1 - count2 > 0:
        parentheses_helper(n, parentheses_lst, word + ')', count1, count2 + 1)


def up_and_right(n, k):
    """
    a function that gives all the right ways to get to a given dot in
    a two dimention way. getting n and k which represents the directions.
    n is the way on the 'x' and k is the way on the 'y'.
    representing the way, we use 'u' for up and 'r' for right.
    :param n: number of 'r' that we needs to move in total
    :param k: number of 'u' that we needs to move in total.
    :return: None, but prints to the user all the ways to get to the given
    parameters.
    """
    if n < 0 or k < 0:
        return
    up_and_right_helper(n, k, '', 0, 0)


def up_and_right_helper(n, k, directions_str, count_n, count_k):
    """
    a function that runs the up and right function, chooses the right ways, then
    it prints them to the user.
    :param directions_str: the string of the directions, starting with nothing
    then building it.
    :param count1: counts the number of times that one direction appeared
    :param count2: counts the number of times that the other direction appeared
    :return: None, but prints to the user.
    """
    # length has to be the length of them together to get to the right point.
    if len(directions_str) == n + k:
        print(directions_str)
    # as long as there are less than we need.
    if count_n < n:
        up_and_right_helper(n, k, directions_str + 'r', count_n+1, count_k)
    if count_k < k:
        up_and_right_helper(n, k, directions_str + 'u', count_n, count_k+1)


def flood_fill(image, start):
    """
    a function that gives the flood fill of a give image,
    allowing to move diagonal or up ,down ,left ,right.
    when it gets to a place it changes the direction form '.'
    to '*'.
    uses the 'flood_fill_helper' function.
    :param image: a given image made of '*' and '.'. represented by list of lists.
    :param start: the starting point to move from.
    :return: None, but changes the given image.
    """
    # so we wont always change the given image, because we need
    # to remember the given image, and the visited places.
    visited_image = copy.deepcopy(image)
    flood_fill_helper(image, start, visited_image)
    # now we can change the image to the visited image,
    # because if finished changing it.
    image = visited_image


def flood_fill_helper(image, start, visited_image):
    """
    a function that runs the 'flood_fill' functions,
    moving to all directions and changing the visited_image,
    according to the places it can get to.
    :param image: a given image made of '*' and '.'. represented by list of lists.
    :param start: the starting point, changes in each iterations, by the functions moves.
    :param visited_image: the image but with changes, for each place the function been at.
    (the starts)
    :return: None , but changes the visited_image lists.
    """
    y, x = start
    # y is the line, x is the column.
    visited_image[y][x] = '*'
    # right to left
    if image[y][x-1] != '*' and visited_image[y][x-1]:
        flood_fill_helper(image, (y, x-1), visited_image)
    # down to up
    if image[y-1][x] != '*' and visited_image[y-1][x] != '*':
        flood_fill_helper(image, (y-1, x), visited_image)
    # up to down
    if image[y+1][x] != '*' and visited_image[y+1][x] != '*':
        flood_fill_helper(image, (y+1, x), visited_image)
    # left to right
    if image[y][x+1] != '*' and visited_image[y][x+1] != '*':
        flood_fill_helper(image, (y, x+1), visited_image)
    else:
        return
