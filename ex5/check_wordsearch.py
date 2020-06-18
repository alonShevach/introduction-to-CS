###############################################################################
# FILE : check_wordsearch.py                                                  #
# WRITER : Alon Shevach , alon.shevach , 20595420                             #
# EXERCISE : intro2cs1 ex5 2018-2019                                          #
# DESCRIPTION: A program that tests the function 'find_words_with_directions, #
# the function is part of the find_words_in_matrix function.                  #
###############################################################################


from wordsearch import *


def test_find_word_with_directions():
    """a function that tests the 'find_words_with_direction' that i created in 'wordsearch' file."""
    matrix = [['g', 'g', 'g', 'g', 'g', 'g'], ['b', 'o', 'b', 'o', 'b', 'o'],
              ['d', 'o', 'g', 'm', 'a', 'g'],
              ['G', 'i', 'E', 'z', 'v', 'b'], ['R', 't', 'r', 'd', 'x', 'n']]
    words = ['dog','bob', 'gbgE', 'gie', 'nbg']
    if (find_word_with_direction(words[0], matrix, 'wr') == 2) and \
        (find_word_with_direction(words[1], matrix, 'lr') == 4)and \
        (find_word_with_direction(words[2], matrix, 'dlr') == 1) and \
        (find_word_with_direction(words[3], matrix, 'udlrwxyz') == 0)and \
        (find_word_with_direction(words[4], matrix, 'wxyzuuuu') == 2):
        return True
    return False


if __name__ == "__main__":
    test_find_word_with_directions()