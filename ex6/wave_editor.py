import copy
import math
import numpy
import scipy
import wave_helper
import os.path

LIST_OF_EXPECTED_INPUTS = ['1', '2', '3', '4', '5', '6']
BAD_FORMATS_MSG = 'Bad Format. Make sure both of the files are wave files\n'
NOT_ENOUGH_FILES_MSG = 'Please enter 2 files arguments\n'
DECODE_COMPO_ERROR = 'Decoding error\n' \
                     'Please write it in the following format:\n' \
                     '[note] [duration] [note] [duration] ...'
REVERSE = '1'
ACCELERATE = '2'
SLOW_DOWN = '3'
CHANGE_VOLUME_UP = '4'
CHANGE_VOLUME_DOWN = '5'
FADE_WAVE = '6'
SAVE_FILE = '1'
ANOTHER_CHANGE = '2'
REVERSE_WAVE = '1'
ACCELERATE_WAVE = '2'
SLOW_DOWN_WAVE = '3'
VOLUME_UP = '4'
VOLUME_DOWN = '5'
CHANGING_WAV_FILE = '1'
COMBINE_2_WAV_FILES = '2'
COMPOSE_A_RHYTHM_FROM_TXT = '3'
EXIT = '4'
FILE_FOR_CHANGE_INPUT = 'Please write down the name of the file you want to change: '
COMPOSITION_FILE_INPUT = 'Please write down the composition text file path: '
TWO_FILES_FOR_COMBINE_INPUT = "Please write down the paths of the two files: "
OUTPUT_FILENAME_INPUT = 'Please write down the name of the saved file: '
TRANSITIONS_MENU_INPUT = 'please choose one of the following actions on the file:\n' \
                         '1. Saving the "wav" file.\n' \
                         '2. Changing the "wav" file.\n' \
                         'Please write down your selection: '
SILENCE = 'Q'
MAIN_INPUT = 'Choose one of the following actions: \n' \
             '1. Changing a "wav" file.\n' \
             '2. Combining 2 "wav" files.\n' \
             '3. Compose a rhythm from text file.\n' \
             '4. Exiting the program. \n' \
             'write down a number from 1-4 that is your choice: '
FILE_CHANGE_INPUT = "Please choose one of the following ways of changing the file:\n" \
                    "1. reverse the 'wav'\n" \
                    "2. accelerate the wave's speed \n" \
                    "3. slow the wave's speed down \n" \
                    "4. turning the volume up \n" \
                    "5. turning the volume down \n" \
                    "6. low pass filter \n" \
                    "please write down the number of your choice: "
BAD_FILE_INPUT = 'Bad file input: the file you gave is not existing,' \
                 'you misspelled his name, or the file format is not the right format.' \
                 ' please try again.'
BAD_INPUT_NUMBER = 'Bad input: you did not choose a valid number.' \
                   ' please try again'
BAD_FILE_PATH_MSG = "Bad file input: one or more of the file's " \
                    "path are incorrect, please try again."
DEFAULT_SPEED_RATE = 2
MIN_AMPLITUDE = -32768
MAX_AMPLITUDE = 32767
AMPLITUDE_FACTOR = 1.2
UP = 1
DOWN = 0
SIXTEENTH_SECOND = 125
DEFAULT_SAMPLE_RATE = 2000
MUSICAL_NOTES_DICT = {'A': 440, 'B': 494, 'C': 523, 'D': 587,
                      'E': 659, 'F': 698, 'G': 784, 'Q': 0}


def main_menu():
    """
    The following function is the main menu that appears to the user,
    it shows a list of choices to make in the program on files.
    :return: None
    """
    user_choice = ''
    # Continues until user chooses to exit.
    while user_choice != EXIT:
        user_choice = input(MAIN_INPUT)
        if user_choice == CHANGING_WAV_FILE:
            changing_a_wav_file_menu()
        elif user_choice == COMBINE_2_WAV_FILES:
            combining_two_wav_files()
        elif user_choice == COMPOSE_A_RHYTHM_FROM_TXT:
            composition_menu()
        elif user_choice != EXIT:
            print(BAD_INPUT_NUMBER)


def changing_a_wav_file_menu(sample_rate=None, wav_lst=None):
    """
    if the user chooses too change the wav file, this function will
    ask him how he want to change it and directs to other
    functions to run the changes
    :param sample_rate:
    :param wav_lst:
    :return: None
    """
    # If sample rate is not none, it means the user already gave us a
    # file name and we do not need to ask him again.
    if sample_rate is None:
        file_name = input(FILE_FOR_CHANGE_INPUT)
        while not (read_wav_file(file_name)):
            # If the file does not exist, or miss spelled,
            # we will ask again for a new file.
            print(BAD_FILE_INPUT)
            file_name = input(FILE_FOR_CHANGE_INPUT)
        sample_rate, wav_lst = read_wav_file(file_name)
    user_change = input(FILE_CHANGE_INPUT)
    while not (user_change in LIST_OF_EXPECTED_INPUTS):
        print(BAD_INPUT_NUMBER)
        # If the number input is wrong, we want to ask the user for another number.
        # Note that if wont ask for another file, if will return the arguments of the
        # last given file.
        user_change = input(FILE_CHANGE_INPUT)
    if user_change == REVERSE_WAVE:
        new_wav = reverse_wave(wav_lst)
    elif user_change == ACCELERATE_WAVE:
        new_wav = accelerate_wave(wav_lst)
    elif user_change == SLOW_DOWN_WAVE:
        new_wav = slow_down_wave(wav_lst)
    elif user_change == VOLUME_UP:
        new_wav = change_volume(wav_lst, UP)
    elif user_change == VOLUME_DOWN:
        new_wav = change_volume(wav_lst, DOWN)
    elif user_change == FADE_WAVE:
        new_wav = fade_wave(wav_lst)
    transition_menu(sample_rate, new_wav)


def composition_menu():
    """
    a menu that appears when
     the user chooses to compose a rhythm from
    a text file.
    :return:
    """
    sample_rate = DEFAULT_SAMPLE_RATE
    compo_file = input(COMPOSITION_FILE_INPUT)
    while (not os.path.isfile(compo_file)) or (not compo_file.endswith('.txt')):
        print(BAD_FILE_PATH_MSG)
        compo_file = input(COMPOSITION_FILE_INPUT)
    composed_wave_lst = read_composition_and_generate_output(compo_file)
    transition_menu(sample_rate, composed_wave_lst)


def transition_menu(sample_rate, wave_lst):
    """a menu that is appearing when the user has already done 1 action,
    then it asks him if he want to make another change or to save the
    changes in a file.
    also saves the file if the user wants."""
    user_choice = input(TRANSITIONS_MENU_INPUT)
    if user_choice == ANOTHER_CHANGE:
        changing_a_wav_file_menu(sample_rate, wave_lst)
    elif user_choice == SAVE_FILE:
        output_filename = input(OUTPUT_FILENAME_INPUT)
        wave_helper.save_wave(sample_rate, wave_lst, output_filename)
    else:
        print(BAD_INPUT_NUMBER)


def combining_two_wav_files():
    """
    The following function combines two wav files into one,
    the function asks for the user to give two wav files, then
    it combines them by using the function united_wave
    :return: new combined  list of wave data
    """
    user_file_path1, user_file_path2 = ask_input_and_set_files()
    # Checking if file is existing.
    # If we have bad file we want to run the function again,
    # to ask for another file,
    sample_rate1, wav_file1 = read_wav_file(user_file_path1)
    sample_rate2, wav_file2 = read_wav_file(user_file_path2)
    combined_sample_rate, combined_wav = united_waves(sample_rate1, sample_rate2, wav_file1,
                                                      wav_file2)
    transition_menu(combined_sample_rate, combined_wav)


def ask_input_and_set_files():
    """
    The following gets 2 files from the user
    and returns them to the caller
    :return: 2 file paths
    """
    files_exists = False
    while not files_exists:
        two_user_files = input(TWO_FILES_FOR_COMBINE_INPUT)
        two_user_files = two_user_files.split()
        if len(two_user_files) != 2:
            print(BAD_FILE_PATH_MSG)
            continue
        user_file_path1 = two_user_files[0]
        user_file_path2 = two_user_files[1]
        if (not  os.path.isfile(user_file_path1)) or (not  os.path.isfile(user_file_path2)):
            print(BAD_FILE_PATH_MSG)
        else:
            files_exists = True
    return user_file_path1, user_file_path2


def read_wav_file(file_name):
    """
    The following function is reading the file and
     returning a tuple of 2 things.
    first one is the sample rate of the file, and the second is the list of the waves.
    :param file_name: a given file
    :return:frame rate,file's content
    """
    wav_file = wave_helper.load_wave(file_name)
    if wav_file == -1:
        return False
    # Dividing the sample rate and the wave_list
    frame_rate, content = wav_file[0], wav_file[1]
    return frame_rate, content


def read_composition_and_generate_output(compo_file):
    """
    The following takes a name of a file which
    has a proper composition format, and turns it
    into a list of generated wave file.
    :param compo_file: file name
    :return: list that represents the composition
             in a wave file
    """
    file = open(compo_file, 'r')
    notes_and_durations_list = list()
    for line in file:
        current_line_data_list = line.split()
        i = 0
        while i + 1 < len(current_line_data_list):
            note = current_line_data_list[i]
            duration = current_line_data_list[i + 1]
            if not duration.isdigit():
                print('Composition file', compo_file, DECODE_COMPO_ERROR)
                return composition_menu()
            elif note not in MUSICAL_NOTES_DICT.keys():
                print("The note", note, 'is not valid!'
                                        ' Please reform your file, valid notes are:\n',
                                        MUSICAL_NOTES_DICT.keys())
                return composition_menu()
            else:
                duration = int(duration)
                notes_and_durations_list.append((note, duration))
                i += 2
    return generate_composition_output(notes_and_durations_list)


def reverse_wave(wave_lst):
    """
    The following function is taking a list
     and reverses it content,
    this way it reverses the waves
    :param wave_lst:
    :return: new reversed list
    """
    # don't change the content of the original list!!
    new_lst = copy.deepcopy(wave_lst)
    return new_lst[::-1]


def accelerate_wave(wave_lst, rate=DEFAULT_SPEED_RATE):
    """
    The following function is getting a list and a rate
     as arguments,
    if the user does not give a rate, the rate will be 2.
    it accelerate it by taking only 1 from the list for each rate
    :param wave_lst:
    :param rate:
    :return: new accelerated wave data
    """

    new_lst = copy.deepcopy(wave_lst)
    return new_lst[::rate]


def create_list_for_average(lst1, lst2, lst3=None):
    """
    The following function gets 3 arguments,
     3 lists and create an average of
    their content. if the user is giving 2 lists it gives the average of
    :param lst1:list number 1
    :param lst2:list number 2
    :param lst3:list number 3 (optional)
    :return: list of averages
    """
    # If we have 3 lists, we need to divide the sum by 3,
    # If we have 2 lists, we need to divide the sum by 2.
    new_list = list()
    for i in range(len(lst1)):
        if lst3:
            new_element = int((lst1[i] + lst2[i] + lst3[i]) / 3)
        else:
            new_element = int((lst1[i] + lst2[i]) / 2)
        new_list.append(new_element)
    return new_list


def slow_down_wave(wave_lst):
    """
    The following function slows down the wave by adding more objects to the list,
    creating a new list which is equal to the previous but
    between 2 objects it inserts the average of them
    :param wave_lst:
    :return: new list of slowed wave date
    """
    new_lst = list()
    average_list = list()
    for i in range(len(wave_lst) - 1):
        # Adding the average of 2 numbers between them.
        average_list.append(create_list_for_average(wave_lst[i], wave_lst[i + 1]))
    for j in range(len(wave_lst)):
        new_lst.append(wave_lst[j])
        if not j > len(average_list) - 1:
            new_lst.append(average_list[j])
    return new_lst


def change_volume(wave_lst, operator):
    """
    The following function function is changing the volume, either turning it up or down
    by the user's choice. using another function 'change_list_elements_vol to
    change to volume for each list inside the list.
    this funtion gets a list and an operator(UP or DOWN)
    :param wave_lst:
    :param operator:
    :return: new list of volume changed wave
    """
    new_lst = list()
    for element in wave_lst:
        new_lst.append(change_list_elements_vol(element, operator))
    return new_lst


def change_list_elements_vol(wave_lst, operator):
    """
    this function changes the volume of each list, given a operator
    which is if it changes the volume up or down
    :param wave_lst:
    :param operator: Volume up \ Volume down
    :return: new wave data
    """
    # for changing the volume up we need to multiply the number with
    # the amplitude factor, to change it down we need to multiply by
    # the reciprocal number of the amplitude factor.
    if operator == UP:
        factor = AMPLITUDE_FACTOR
    else:
        # volume down
        factor = 1 / AMPLITUDE_FACTOR
    new_lst = list()
    for element in wave_lst:
        new_element = element * factor
        # Checking that after changing the volume, it wont pass the maximum
        # or minimum amplitude allowed.
        if new_element > MAX_AMPLITUDE:
            new_element = MAX_AMPLITUDE
        # if it reaches to lowest volume
        elif new_element < MIN_AMPLITUDE:
            new_element = MIN_AMPLITUDE
        new_lst.append(int(new_element))
    return new_lst


def fade_wave(wave_lst):
    """
    this function is doing a 'fade' to the given wave.
    it recieves a list of the wave
    :param wave_lst: a list of wave data
    :return: new faded wave
    """
    faded_lst = list()
    if len(wave_lst)==0:
        return []
    for i in range(len(wave_lst)):
        # If the number is in the beginning or the end of the list,
        # we need to make a average of it and the number next to it.
        if i == 0 and len(wave_lst)>1:
            element = create_list_for_average(wave_lst[i], wave_lst[i + 1])
        elif i == (len(wave_lst) - 1):
            element = create_list_for_average(wave_lst[i - 1], wave_lst[i])
        else:
            element = create_list_for_average(wave_lst[i - 1], wave_lst[i], wave_lst[i + 1])
        faded_lst.append(element)
    return faded_lst


def united_waves(sample_rate1, sample_rate2, wave_lst1, wave_lst2):
    """
    this function combines the sample rates of 2 files and
    the waves of 2 files.
    the funtion receives the 2 sample rates and the 2 list of waves.
    uses the funtion generate_relevant_list
    :param sample_rate1: sample rate of wave 1
    :param sample_rate2: samvple rate of wave 2
    :param wave_lst1: wave 1
    :param wave_lst2: wave 2
    :return: united wave file
    """
    # If the sample rates are equal it doesnt matter who we choose,
    # Else we need to check who is higher to make the new wave list.
    if sample_rate1 == sample_rate2:
        return sample_rate2, wave_union(wave_lst1, wave_lst2)
    elif sample_rate1 > sample_rate2:
        relevant_list = generate_relevant_list(wave_lst1, sample_rate1, sample_rate2)
        return sample_rate2, wave_union(relevant_list, wave_lst2)
    else:
        relevant_list = generate_relevant_list(wave_lst2, sample_rate2, sample_rate1)
        return sample_rate1, wave_union(relevant_list, wave_lst1)


def generate_relevant_list(wave_lst1, sample_rate1, sample_rate2):
    """
    The function gets a list and 2 sample rates, and then creates
    a new list for the relevant objects according to the sample rates
    :param wave_lst1:
    :param sample_rate1:sample rate of list 1
    :param sample_rate2: sample rate of list 2
    :return: relevant chunk in list 1
    """
    common_divisor = gcd(sample_rate1, sample_rate2)
    block_sample = int(sample_rate1 / common_divisor)
    relevant_elements = int(sample_rate2 / common_divisor)
    relevant_list = list()
    for i in range(0, len(wave_lst1), block_sample):
        relevant_list += wave_lst1[i:relevant_elements + i]
    return relevant_list


def wave_union(wave_lst1, wave_lst2):
    """
    this function combine 2 wave lists using the create_list_for_average
    function, and returns the combined list
    :param wave_lst1: wave 1
    :param wave_lst2: wave 2
    :return: combined list
    """
    united_lst = list()
    count = 0
    for i in range(min(len(wave_lst1), len(wave_lst2))):
        new_element = create_list_for_average(wave_lst1[i], wave_lst2[i])
        united_lst.append(new_element)
        count += 1
    # counting the number of elements added to list, to add the rest of them.
    united_lst += max_list(wave_lst1, wave_lst2)[count:]
    return united_lst


def max_list(lst1, lst2):
    """
    a simple function that checks which list is longer, and return the longer list.
    :param lst1: list 1
    :param lst2: list 2
    :return: the longer list
    """
    if len(lst1) > len(lst2):
        return lst1
    else:
        return lst2


def gcd(x, y):
    """
    a function that gives the greatest common divisor of 2 numbers, according,
    the gcd algorithm
    :param x: num x
    :param y: num y
    :return: greatest common divisor of x and y
    """
    while y > 0:
        x, y = y, x % y
    return x


def generate_composition_output(compo_input):
    """
    this function gets a composition input and create a wave list according
    to the given compositions.
    :param compo_input:
    :return: composition wave output (as a list)
    """
    wave_file = list()
    for element in compo_input:
        note, duration = element
        wave_file.extend(generate_wave_from_range_and_note(note, duration))
    return wave_file


def generate_wave_from_range_and_note(note, duration):
    """
    The following function creates a wave list from given 'notes' and 'durations'
    and then returns the list of them.
    :param note: a single note
    :param duration: time for a single note
    :return: a single wave data list the represents the note
             sound in a specific duration

    """
    wave = list()
    if note == SILENCE:
        return [[0, 0]] * (duration * SIXTEENTH_SECOND)
    samples_per_cycle = DEFAULT_SAMPLE_RATE / MUSICAL_NOTES_DICT[note]
    for i in range(duration * SIXTEENTH_SECOND):
        value = int(MAX_AMPLITUDE * math.sin(math.pi * 2 * (i / samples_per_cycle)))
        wave.append([value] * 2)
    return wave


if __name__=='__main__':
     	main_menu()
