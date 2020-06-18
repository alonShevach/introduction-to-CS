################################################################################################
# FILE : check_update_word_pattern.py                                                          #
# WRITER : alon shevach , alon.shevach , 20595420                                              #
# EXERCISE : intro2cs1 ex4 2018-2019                                                           #
# DESCRIPTION: A program that tests the function "update_word_pattern in the hangman.py file   #
################################################################################################

from hangman import update_word_pattern
#to import the function for testing it


def test_update_word_pattern():
    """a function that tests the function "update_word_pattern" in hangman.py."""
    if (update_word_pattern('revive', '______', 'e') == '_e___e') and\
    (update_word_pattern('revive', '_e___e', 'e') == '_e___e') and \
    (update_word_pattern('fffff','_____','f') == 'fffff') and\
    (update_word_pattern('victory', '_______', 'b') == '_______'):
        print ('Function "update_word_pattern" test success')
        return True
    print ('Function "update_word_pattern" test fail')
    return False


if __name__ == '__main__':
    #to make it not run everytime importing
    test_update_word_pattern()

