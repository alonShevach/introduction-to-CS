#################################################################
# FILE : wordsearch.py                                          #
# WRITER : Alon Shevach , alon.shevach , 20595420               #
# EXERCISE : intro2cs1 ex5 2018-2019                            #
# DESCRIPTION: A program that runs the known word search on a   #
# matrix chosen by user, and that is running from commandline   #
#################################################################


import sys
import os.path

THE_CORRECT_DIRECTIONS = 'udlrwxyz'
BAD_NUMBER_OF_ARGS = 'the function did not recieve the right ' \
                     'amount of arguments, reviewed more than 4, or less than 4'
EXPECTED_NUM_OF_ARGS = 4
BAD_DIRECTIONS = "directions should be one or more of " \
                 "the following letters:" \
                 "'u','d','l','r','w','x','y','z', the " \
                 "choice was not a combination of those letters."
BAD_WORD_FILE_INPUT = "file missing :the word_list file " \
                      "is missing, or his name or path are not spelled right. "
BAD_MATRIX_FILE = "file missing :the matrix file " \
                  "is missing, or his name or path are not spelled right. "
UP = 'u'
DOWN = 'd'
LEFT = 'l'
DOWN_RIGHT = 'y'
DOWN_LEFT = 'z'
UP_RIGHT = 'w'
UP_LEFT = 'x'


def main(args):
    """The main function that runs all the other functions for the word search
    the function is getting the 'args' which the user printed in the shell/cmd"""
    msg = check_input_args(args)
    # Msg is None when all the args are as we expected, if not, we cant play the game.
    if msg is not None:
        return
    word_list_filename = args[0]
    mat_filename = args[1]
    output_filename = args[2]
    directions = args[3]
    matrix = read_matrix_file(mat_filename)
    word_list = read_wordlist_file(word_list_filename)
    results = find_words_in_matrix(word_list, matrix, directions)
    write_output_file(results, output_filename)


def check_input_args(args):
    """A function to check the input args that the user printed in the shell/cmd.
    the expected args are 2 existing files, name of a newfile to create,
    and 1 or more from the 'direction' letters 'THE_CORRECT_DIRECTIONS'"""
    if len(args) != EXPECTED_NUM_OF_ARGS:
        return BAD_NUMBER_OF_ARGS
    # This function checks if the file exists, if not, the game stops and giving the
    # Bad file note
    if not os.path.isfile(args[0]):
        return BAD_WORD_FILE_INPUT
    if not os.path.isfile(args[1]):
        return BAD_MATRIX_FILE
    for i in range(len(args[3])):
        # Directions must be 1 of the 8
        if not args[3][i] in THE_CORRECT_DIRECTIONS:
            return BAD_DIRECTIONS
    return None


def read_wordlist_file(filename):
    """A function for reading the given wordlist file."""
    f = open(filename)
    word_list = f.read().splitlines()
    f.close()
    return word_list


def read_matrix_file(filename):
    """A function to read the given matrix file"""
    f = open(filename)
    matrix = []
    file_input = f.read().splitlines()
    for word in file_input:
        letter_lst = word.split(',')
        # Creating the matrix without the ','
        matrix.append(letter_lst)
    f.close()
    return matrix


def find_words_in_matrix(word_list, matrix, directions):
    """The function finds the words in the matrix, using another function which runs the
    search with given directions, this function returns the results of the searches."""
    results = []
    word_count = 0
    # Remove duplicates by inserting the list to set, and converting it back to list
    no_duplicates_directions = list(set(directions))
    if (not matrix) or (not word_list) or (not no_duplicates_directions):
        return results
    for word in word_list:
        for direction in no_duplicates_directions:
            # The "find_words_with_direction function will count
            # The number of times a 'word' appeared in the given directions.
            word_count += find_word_with_direction(word, matrix, direction)

            # If this is the last direction given, we would like to add the
            # Number of times he appeared in all the directions to the results list.
            if direction == no_duplicates_directions[-1]:
                # If he did not find we should not add anything to the list.
                if word_count == 0:
                    continue
                results.append((word, word_count))
                # Resetting the count for the new word.
                word_count = 0
    return results


def write_output_file(results, output_filename):
    """A function to create and write an output file with
    all the results of the word search"""
    f = open(output_filename, 'w')
    if not results:
        f.close()
        return
    for word, count in results:
        f.write(word + ',' + str(count) + '\n')
    f.close()


def find_word_with_direction(word, matrix, direction):
    """Finding the word from the matrix with the given directions.
    diverting the matrix to the right angle for the direction to become like
    it is from left to right. i used all the functions to rotate the
    matrix into the right position."""
    count = 0
    new_matrix = matrix[:]
    if direction == DOWN:
        new_matrix = create_line_for_downwards(matrix)
    elif direction == LEFT:
        new_matrix = reverse_matrix_lines(matrix)
    elif direction == UP:
        new_matrix = matrix_turn_upside_down(matrix)
        new_matrix = create_line_for_downwards(new_matrix)
    elif direction == DOWN_RIGHT:
        new_matrix = create_full_diagonal_matrix(matrix)
    elif direction == UP_LEFT:
        new_matrix = reverse_whole_matrix(matrix)
        new_matrix = create_full_diagonal_matrix(new_matrix)
    elif direction == UP_RIGHT:
        new_matrix = matrix_turn_upside_down(matrix)
        new_matrix = create_full_diagonal_matrix(new_matrix)
    elif direction == DOWN_LEFT:
        new_matrix = reverse_matrix_lines(matrix)
        new_matrix = create_full_diagonal_matrix(new_matrix)
    # Counting the times a word occurs from the new matrix(all direction become
    # From left to right
    count += find_word_from_left_to_right_in_matrix(word, new_matrix)
    return count


### Helper Functions ###


def create_line_for_downwards(matrix):
    """The function creates a list of the downwards line of the matrix."""
    downwards_lines = []
    temporary_list = []
    for i in range(len(matrix[0])):
        for line in matrix:
            temporary_list.append(line[i])
            if len(temporary_list) == len(matrix):
                downwards_lines.append(temporary_list)
                temporary_list = []
    return downwards_lines


def reverse_matrix_lines(matrix):
    """A function to reverse all the lines in the matrix"""
    reversed_matrix = []
    for line in matrix:
        reversed_matrix.append(line[::-1])
    return reversed_matrix


def matrix_turn_upside_down(matrix):
    """A simple function to turn the matrix upside down"""
    # This could be simplified not to be a function, but to remain consistent
    # with all the other functions and to create a clean code, i made it a function.
    return matrix[::-1]


def reverse_whole_matrix(matrix):
    """A function to turn the matrix upside down, then to reverse every line too."""
    new_matrix = matrix_turn_upside_down(matrix)
    reversed_matrix = reverse_matrix_lines(new_matrix)
    return reversed_matrix


def create_full_diagonal_matrix(matrix):
    """A function that creates a list of all the diagonal lines in the matrix
    using the 'down right' direction (from top left to down right)
    we will use this function to create all kinds of diagonal lines."""
    # Creating half of the diagonal line
    half_diagonal_matrix = create_half_diagonal_matrix(matrix)
    new_matrix = create_line_for_downwards(matrix)
    # Turning the matrix upside down so the other half will be in the same place
    complete_diagonal_matrix = create_half_diagonal_matrix(new_matrix)
    for i in range(len(half_diagonal_matrix)):
        if half_diagonal_matrix[i] in complete_diagonal_matrix:
            # adding both list together, without the 1 line that is common
            # to both of them
            continue
        complete_diagonal_matrix.append(half_diagonal_matrix[i])
    return complete_diagonal_matrix


def create_half_diagonal_matrix(matrix):
    """This function creates a list of a part of diagonal lines
    the part which is from the primary matrix diagonal and down
    (not include the diagonals that are above the primary diagonal line.)"""
    # I created a temporary list to bond every diagonal line at once,
    # If i would not do it the list was with 1 object, i found it more efficient
    diagonal_list = []
    temporary_list = []
    for i in range(len(matrix)):
        # Not doing it on the first run, reset it for each line
        if i > 0:
            diagonal_list.append(temporary_list)
            temporary_list = []
        for index, line in enumerate(matrix[i:]):
            # Not passing the indexes of the line
            if index >= len(matrix[0]):
                continue
            temporary_list.append(line[index])
    diagonal_list.append(temporary_list)
    return diagonal_list


def find_word_from_left_to_right_in_matrix(word, matrix):
    """This is the function that searches the words in the lines,
    it searches from left to right only. uses another function to
    find words in a single matrix line"""
    word_count = 0
    for line in matrix:
        # Running for indexes, to find a letter that fits the first letter of the word,
        # When it finds, run the other function to see if the word is in the line.
        for i in range(len(line)):
            # If the word is in the line.
            if line[i] == word[0] and (find_word_from_left_to_right_in_line(word, line[i:])):
                word_count += 1
    return word_count


def find_word_from_left_to_right_in_line(word, line):
    """A function to find the word in a single line."""
    count = 0
    # The word cant be in the line if it is longer than the line.
    if len(word) > len(line):
        return False
    for j in range(len(word)):
        if line[j] == word[j]:
            # Counting the number of letters that are in the line and in the word.
            count += 1
    # If all the letters are the same, the word is in the line.
    if count == (len(word)):
        return True
    return False


if __name__ == "__main__":
    main(sys.argv[1:])
