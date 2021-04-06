#############################################################
# FILE : hangman.py                                         #
# EXERCISE : intro2cs1 ex4 2018-2019                        #
# DESCRIPTION: A program that runs the known hangman game   #
#############################################################

import hangman_helper


CHAR_A = 97
LETTERS_COUNT = 26
BAD_INPUT = 'bad input'
HINT = 'hint'


def main():
    """the main function that runs the game by using the run_single_game function."""
    words_list = hangman_helper.load_words()
    run_single_game(words_list)
    another_game = define_input()
    while another_game:
        # the loop runs as long as the user wants to keep playing
        run_single_game(words_list)
        another_game = define_input()


def run_single_game(words_list):
    """a function for running a single hangman game"""
    msg = hangman_helper.DEFAULT_MSG
    # Get a random word
    random_word = hangman_helper.get_random_word(words_list)
    wrong_guess_lst = []
    # Set the string as _ of the same length as the word
    pattern = '_' * len(random_word)
    error_count = 0
    while (pattern != random_word) and (error_count < hangman_helper.MAX_ERRORS):
        # As long as the player wont find the word by guessing the correct letters,
        # or if the player will wrong guess more than the maximum guesses allowed,
        # the function will keep on asking for letters or hints.
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, False)
        user_input = define_input()
        if user_input == HINT:
            msg = hangman_helper.HINT_MSG + hint(words_list, pattern, wrong_guess_lst)
            hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, False)
            # If the player will asks for a hint, the hint function will run and find the correct letter
            # and print it to the users screen along with the HINT_MSG
        elif user_input == BAD_INPUT:
            msg = hangman_helper.NON_VALID_MSG
            # If the user will give anything that is not a 1 lower english letter, we will print the NON_VALID_MSG
        else:
            # If user chose a legitimate letter according to the requirements
            if (user_input in pattern) or (user_input in wrong_guess_lst):
                # If the player chose a letter he already chosen before,
                # it will check if the letter is already in the pattern or if it is in the wrong_guess_lst
                msg = hangman_helper.ALREADY_CHOSEN_MSG + user_input
                continue
            # If it is a legitimate letter and the player chooses it for the 1st time
            # the letter pattern will be updated.
            if user_input in random_word:
                # If he guessed right, the pattern will be changed.
                pattern = update_word_pattern(random_word, pattern, user_input)
            else:
                # The word is not in the list, meaning a wrong guess
                wrong_guess_lst.append(user_input)
                error_count = len(wrong_guess_lst)
            msg = hangman_helper.DEFAULT_MSG
    if error_count == hangman_helper.MAX_ERRORS:
        # If the user passed the maximum allowed wrong guesses, he lost.
        msg = hangman_helper.LOSS_MSG + random_word
    else:
        # If he did not lose he won, because the 'while' stopped.
        msg = hangman_helper.WIN_MSG
    # Now we will ask the player for another game.
    hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, True)


def update_word_pattern(word, pattern, letter):
    """a function that updates the word pattern according to the user's new guess"""
    pattern_list = list(pattern)
    # Makes the pattern a list so we will be able to change it values.
    for i in range(len(word)):
        if word[i] == letter:
            # If the guessed letter is in the word.
            pattern_list[i] = word[i]
    # Make the pattern to a string again, because the pattern should be a string.
    return str.join('', pattern_list)


def define_input():
    """define if the input is a hint, a letter or a 'play again'."""
    input_kind, input_val = hangman_helper.get_input()
    if input_kind == hangman_helper.HINT:
        return HINT
    elif (input_kind == hangman_helper.LETTER) and (check_valid_letter(input_val)):
        return input_val
    elif input_kind == hangman_helper.PLAY_AGAIN:
        return input_val
    return BAD_INPUT


def check_valid_letter(user_input):
    """checking if a letter is following the requirements, being a single lower english letter"""
    if (len(user_input) != 1) and (type(user_input) != str):
        return False
    for i in range(LETTERS_COUNT):
        any_letter = index_to_letter(i)
        if any_letter == user_input:
            return True
    return False


def hint(words_list, pattern, wrong_guess_lst):
    """a function that gives a player his hint. running a function to check which words fits the pattern,
    then checks the most common letter in the list of words"""
    words = filter_words_list(words_list, pattern, wrong_guess_lst)
    return choose_letter(words, pattern)


def filter_words_list(words, pattern, wrong_guess_lst):
    """a function that finds a list of words that fits to the pattern from a given list of words."""
    new_lst = []
    for word in words:
        if len(word) == len(pattern) and check_single_word_hint(word, pattern, wrong_guess_lst):
            new_lst.append(word)
    return new_lst


def check_single_word_hint(word, pattern, wrong_guess_lst):
    """a function to check if the pattern fits to a single word,
     according to the user's wrong guesses and right guesses"""
    common_letter = []
    for i in range(len(word)):
        if pattern[i] != '_':
            if pattern[i] != word[i]:
                return False
            else:
                common_letter.append(pattern[i])
    if not check_letter_in_word(common_letter, word, pattern) or not \
            check_letter_in_word(wrong_guess_lst, word, pattern):
        return False
    return True


def check_letter_in_word(letter_lst, word, pattern):
    """a function to check if the word fits according to the user's right previous guesses"""
    for i in range(len(word)):
        for letter in letter_lst:
            if letter == word[i] and letter != pattern[i]:
                return False
    return True


def choose_letter(words_lst, pattern):
    """a function to find the right letter to give as a hint to the user from a list of words."""
    biggest = 0
    strongest_letter = None
    for i in range(LETTERS_COUNT):
        letter = index_to_letter(i)
        if letter in pattern:
            continue
        count = letter_in_list_of_words(words_lst, letter)
        if count > biggest:
            biggest = count
            strongest_letter = letter
    return strongest_letter


def letter_in_word(word, letter):
    """a function that counts how many times a letter is in a single word"""
    count = 0
    for alphabet in word:
        if alphabet == letter:
            count += 1
    return count


def letter_in_list_of_words(words_lst, letter):
    """a function that calculates how many times is a letter in list of words,
    using the letter_in_word function"""
    count = 0
    for word in words_lst:
        count += letter_in_word(word, letter)
    return count


def letter_to_index(letter):
    """return the index of the given letter in an alphabet list."""
    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
    """return the letter corresponding to the given index"""
    return chr(index + CHAR_A)


if __name__ == "__main__":
    #to make it not run everytime importing
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()
