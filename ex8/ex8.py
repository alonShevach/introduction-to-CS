###################################################################################
# FILE : ex8.py                                                                   #
# EXERCISE : intro2cs1 ex8 2018-2019                                              #
# DESCRIPTION: part 1: the sudoku solver, which uses solves the known sudoku game.#
# which uses solves the known sudoku game.                                        #
# part 2: 3 functions that are based on a function form the tirgul,               #
# with some changes we've asked to do                                             #
###################################################################################


######################################
###########Sudoko Functions###########
######################################

import copy
import generate_random_sudoku
EMPTY_SLOT = 0


def solve_sudoku(board):
    """
    a function that solves a sudoku board according to the sudoku game.
    :param board: a list of lists, which each list represents the line on the
    sudoku board, the board columns and lines has to be equal, and has to be a
    squared natural number.
    :return: return True if the sudoku is solvable, if not returns False,
    also if True it changes the board to the solution board.
    """
    n = len(board[0])
    # Creates a dictonary with the numbers in the soduku(numbers from 1 to n).
    times_appeared_dict = {element: 0 for element in range(1, n + 1)}
    # Creates a "board" for the squares inside the soduko.
    sub_board = make_subboards_from_board(board)
    # Creates a "board for the downward lines in the soduko.
    downwards_lines = create_line_for_downwards(board)
    # now we update the dictonary according to the number of times each number appears.
    for line in board:
        for i in range(1, n+1):
            if i in line:
                times_appeared_dict[i] += 1
    # Create a list that is sorted by the number of times each number appears in the board.
    # From the smallest appeared num to the biggest appeared.
    # I found it much more efficient to go over the numbers starting from
    # the 1 that appeared the most.
    sorted_list = create_a_sorted_list_from_dict(times_appeared_dict)
    # so we wont change the board, because if there is no solution we have to leave
    # the board the same.
    playable_board = copy.deepcopy(board)
    # sort it from the biggest to the smallest.
    sorted_list = sorted_list[::-1]
    solve_sudoku_helper(playable_board, downwards_lines, sub_board,
                        0, 0, sorted_list[0], n, [], times_appeared_dict, sorted_list, 0)
    # If all the numbers in the dictonary are n, it means the board is full.
    if checks_if_all_values_are_n_in_dict(times_appeared_dict, n):
        board = playable_board
        for line in playable_board:
            print(line)
        return True
    # if the board is not full, it cannot be filled.
    return False


def create_a_sorted_list_from_dict(dict):
    """
    creates a list for the keys with the biggest value.
    :param dict: a dictonary
    :return: a sorted list of keys, sorted by thier values, from smallest to biggest..
    """
    sorted_by_value = sorted(dict.items(), key=lambda kv: kv[1])
    sorted_list = []
    for i in range(len(dict)):
        sorted_list.append(sorted_by_value[i][0])
    return sorted_list


def solve_sudoku_helper(playable_board, downwards_lines, sub_board,
    sub_board_index, line_in_sub_board_index, num, n, failed,
                        times_appeared_dict, sorted_list, index):
    """
    the function that checks for the solution to the soduko, it updates the list
    according to the solution if the board has solution, if not, it returns.
    :param playable_board: the board we update.
    :param downwards_lines: a list of the downword lines in the board
    :param sub_board: a list of all the square's lists.
    :param sub_board_index: the square's index which we check in
    :param line_in_sub_board_index: the index inside the square, on the squares in
    the soduko
    :param num: number we now put in the board according to the sudoku rules.
    :param n: the size of the board's line, the board is nxn
    :param failed: A parameter to let the function know if it found solution in the
    path checked, if not it will go for another way.
    i chose it to be a list so it will be mutable, and will be changed easly.
    :param times_appeared_dict: a dictonary for the numbers in the board,
    showing how many times each 1 appears.
    :param sorted_list: a list of numbers, sorted by the most appeared
    number to the less appeared number
    :param index: index for the number in the sorted list.
    :return:
    """
    if failed:
        return
    # base case, if the number appears the max of times it should,
    # and this is the last number, return.
    if times_appeared_dict[num] == n:
        if num == sorted_list[n-1]:
            return
        # if it is not the last number, go the the next 1.
        index += 1
        num = sorted_list[index]
        sub_board_index = 0
        line_in_sub_board_index = 0
    # if it reached the index after the last number in the list inside the list,
    # it mean it did not place the number(because it did not returned.
    # so it failed putting the number.
    if line_in_sub_board_index == n:
        failed.append(True)
        return
    # if the number is already in the square, we will go the next square
    # until it wont be in the square.
    for i in range(sub_board_index, len(sub_board)):
        if num in sub_board[sub_board_index]:
            sub_board_index += 1
            line_in_sub_board_index = 0
        else:
            break
    # if we passed the last square, and if the number appears the maximum timed it should,
    # if this is the last number, we return, if it is not, we will pass to the next.
    # and if the number does not appear maximum times, it means we failed putting it.
    if sub_board_index == n:
        if times_appeared_dict[num] == n:
            if num == sorted_list[n-1]:
                return
            index += 1
            num = sorted_list[index]
            sub_board_index = 0
            line_in_sub_board_index = 0
        else:
            failed.append(True)
            return
    # the function find the location of the place we are at, by the line and column,
    # so we will be able to see if we can place it.
    line_index, column_index = find_number_location_line_and_column(sub_board_index,
                                                                    line_in_sub_board_index, n)
    # as long as the slot we are at is not empty, nor the number appears in the column,
    # or appears in the line, we will go to the next index.
    while sub_board[sub_board_index][line_in_sub_board_index] != EMPTY_SLOT or not \
            check_if_number_fits(playable_board, downwards_lines, column_index, line_index, num):
        line_in_sub_board_index += 1
        # if we passed the last index, means we can not place the number, means it failed.
        if line_in_sub_board_index == n or sub_board_index == n:
            failed.append(True)
            return
        line_index, column_index = find_number_location_line_and_column(sub_board_index,
                                                                        line_in_sub_board_index, n)
    # we place the number in the location we are at, because it fits all the
    # conditions according to the game. we will update the lists in the right place.
    update_boards(playable_board, sub_board, downwards_lines, line_index, column_index,
                  sub_board_index, line_in_sub_board_index, num)
    # updating the dictonary.
    times_appeared_dict[num] += 1
    # and now we want to go again, in the next square in the sudoku.
    solve_sudoku_helper(playable_board, downwards_lines, sub_board, sub_board_index + 1,
                        0, num, n, failed, times_appeared_dict, sorted_list, index)
    # When we get back here, after the recursion, we check if we failed in the way.
    # if we did, when we are here it will be after we updated the sudoku,
    # so we cant undo the change and try again from the next index.
    if failed and not (checks_if_all_values_are_n_in_dict(times_appeared_dict, n)):
        # removing the last number placed.
        update_boards(playable_board, sub_board, downwards_lines, line_index, column_index,
                      sub_board_index, line_in_sub_board_index, EMPTY_SLOT)
        times_appeared_dict[num] -= 1
        failed = []
        solve_sudoku_helper(playable_board, downwards_lines, sub_board, sub_board_index,
            line_in_sub_board_index + 1, num, n, failed, times_appeared_dict, sorted_list, index)


def find_number_location_line_and_column(sub_board_index, index, n):
    """
    a function that finds the number in the board's line and column, according
    to the number's place in the square.
    :param sub_board_index: the index of the square
    :param index: the index inside the square
    :param n: the length of the line and square.
    :return: the line index in the board and the column index in the board.
    """
    y = sub_board_index % (n**0.5)
    line_index = int(index//(n**0.5) + y*(n**0.5))
    x = index % (n**0.5)
    column_index = int((sub_board_index // (n**0.5))*(n**0.5) + x)
    return line_index, column_index


def make_subboards_from_board(board):
    """
    a function for making the squares inside the sudoku according
    to the game rules, squares size of (n**0.5)x(n**0.5)
    :param board: the board of the game
    :return: the list of the squares.
    """
    subboard_lst = []
    temporary_lst = []
    subboard_size = int(len(board)**0.5)
    for i in range(int(subboard_size)):
        for line in board:
            if len(temporary_lst) == len(board[0]):
                subboard_lst.append(temporary_lst)
                temporary_lst = []
            line_for_sub = line[subboard_size*i:subboard_size+subboard_size*i]
            for num in line_for_sub:
                temporary_lst.append(num)
        if len(temporary_lst) == len(board[0]):
            subboard_lst.append(temporary_lst)
            temporary_lst = []
    return subboard_lst


def create_line_for_downwards(board):
    """
    The function creates a list of the downwards line of the board.
    """
    downwards_lines = []
    temporary_list = []
    for i in range(len(board[0])):
        for line in board:
            temporary_list.append(line[i])
            if len(temporary_list) == len(board):
                downwards_lines.append(temporary_list)
                temporary_list = []
    return downwards_lines


def checks_if_all_values_are_n_in_dict(dict, n):
    """
    this function checks if all the values of the numbers in the
    dict are n, from a given number.
    :param dict: a dictonary.
    :param n: number for the values to be equal to
    :return: if the values are equal to n in all the dict, True,
    if not it returns False.
    """
    for key, value in dict.items():
        if value != n:
            return False
    return True


def check_if_number_fits(playable_board, downwards_lines, column_index, line_index, num):
    """
    checks if number fits according to the sudoku rules, not having the same number in the
    column, in the line and in the square.
    :return: True if it fits according to the rules,
    False if it does not fit.
    """
    if (num in playable_board[line_index]) or (num in downwards_lines[column_index]):
        return False
    return True


def update_boards(board, sub_board, downwards_lines, line_index, column_index,
                  sub_board_index, line_in_sub_board_index, num):
    """
    a function that updates the board(putting the number in the board.
    and updates all the lists of lines and column and square of the board.
    :param board: the board to update.
    :param sub_board: the squares inside the board
    :param line_index: index of the place we want ot update, in the board line.
    :param column_index: the index of the place we want to update, in the board column
    :param sub_board_index: the index of the square
    :param line_in_sub_board_index: the place inside the square.
    :param num: the number we want to put in the board, and update in the lists.
    :return: only updates the lists. returns None
    """
    board[line_index][column_index] = num
    sub_board[sub_board_index][line_in_sub_board_index] = num
    downwards_lines[column_index][line_index] = num


##########################################
################Part two##################
##########################################


def print_k_subsets(n, k):
    """
    a function that gets n and k natural numbers, and prints all the
    different kind of lists that can be made out of range(n) while the list
    has to be sorted from lowest to highest
    :param n: range to go on.
    :param k: the length of the lists to print
    :return: None, but prints to the user.
    """
    if k == 0:
        print ([[]])
        return
    if k <= n:
        cur_set = [False]*n
        k_subsets_helper(cur_set, k, 0, 0)
    else:
        print ([])


def k_subsets_helper(cur_set, k, index, picked, lst=None):
    """
    a function that finds all the different lists can be make
    from range(n) according to the rules.
    :param cur_set: list of lists with True and False values
    :param k: length of list neccesary
    :param index: index to go on the list.
    :param picked: the index of picked objects
    :param lst: if given, is a list to be filled with the lists.
    :return: None, but prints or updates a given list.
    """
    if k == picked:
        if lst is None:
            print_or_update_set(cur_set)
            return
        print_or_update_set(cur_set, lst)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    k_subsets_helper(cur_set, k, index + 1, picked + 1, lst)
    cur_set[index] = False
    k_subsets_helper(cur_set, k, index + 1, picked, lst)


def print_or_update_set(cur_set, lst=None):
    """
    a function that prints the indexes of the cur_set with the
    True values, or saves the indexes and update them to a given list.
    :param cur_set: list of lists with bool expressions
    :param lst: if given, a list to update.
    :return: returns None, but updates a given list, or prints to the user.
    """
    temporary_lst = []
    for index, in_cur_set in enumerate(cur_set):
        if in_cur_set:
            temporary_lst.append(index)
    if lst is None:
        print(temporary_lst)
    else:
        lst.append(temporary_lst)
    return


def fill_k_subsets(n, k, lst):
    """
    a function that adds the k_subset of n in length k
    to a given empty list.
    :param n: range to go on
    :param k: length of list in the list.
    :param lst: a given empty list to update.
    :return: None, but updates the list.
    """
    if k <= n:
        cur_set = [False]*n
        k_subsets_helper(cur_set, k, 0, 0, lst)


def return_k_subsets(n, k):
    """
    a function that does the k_subsets of n in length k,
    but this time not passing any list to the other functions of the recursion
    :param n: range to go on
    :param k: length of list
    :return: the list of lists, according to the k_subset rules.
    """
    if k == 0:
        return [[]]
    if k <= n:
        temporary_lst = return_k_subsets_helper(n, k, 0)
        results = []
        # gives only the lists in length k.
        for lst in temporary_lst:
            if len(lst) == k:
                results.append(lst)
        return results
    else:
        return []


def return_k_subsets_helper(n, k, picked):
    """
    a function that uses recursion for giving the k_subset without
    having a list as an argument.
    :param n: range to go on
    :param k: length of lists in the list
    :param picked: the object we have already picked.
    :return: the list of k_subset, but not in the length of k.
    """
    if picked == k:
        return [[]]
    res = []
    for i in range(n):
        temporary_lst = return_k_subsets_helper(n, k, picked+1)
        for lst in temporary_lst:
            if lst and i <= lst[-1]:
                continue
            lst.append(i)
        res += temporary_lst
    return res

if __name__ == "__main__":
    s = generate_random_sudoku.generate_sudoku()
    print("the sudoku: ")
    for line in s:
        print(line)
    print("solution: ")
    solve_sudoku(s)
