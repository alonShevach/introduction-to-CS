################################################################
# FILE : ex11.py                                               #
# WRITER : alon shevach , alon.shevach , 20595420              #
# EXERCISE : intro2cs1 ex11 2018-2019                          #
# DESCRIPTION: 3 class types, Node, Record and Diagnoser,      #
# and 2 functions, one that builds a tree, another that builds #
# the most optimal tree according to the given arguments.      #
################################################################

import itertools

class Node:
    """
    a class that represents each dot of the tree. having the next dots as
    positive child and negative child, linked to it.
    """
    def __init__(self, data, pos=None, neg=None):
        """
        the constractor of the class.
        :param data: the data in each dot in the tree.
        :param pos: the positive child, another Node type.
        if it has no child, it is None
        :param neg: the negative child. a Node type , if there is no
        negative child, it is None.
        """
        self.data = data
        self.positive_child = pos
        self.negative_child = neg


class Record:
    """
    a class that has an illness and its symptoms.
    saved in the constractor as symptoms and illness.
    """
    def __init__(self, illness, symptoms):
        """
        the constractor of the class.
        :param illness: a str that is an illness.
        :param symptoms: list of strings, that represents the
        symptoms of the illness.
        """
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """
    a function that receives a filepath, and returns the records in the
    file. as a record type.
    :param filepath:
    :return:
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """
    a class that gets a tree root and have methods on that given tree.
    """
    def __init__(self, root):
        """
        the constractor of the class.
        :param root: a Node type root of a tree.
        """
        self.root = root

    def diagnose(self, symptoms):
        """
        a function that diagnose from the tree in the constactor, the
        illness that fits the given symptoms, according to the tree.
        :param symptoms: a list of strings, that are the symptoms of
        the illness.
        :return: the illness that fits the most to the symptoms.
        """
        temp_node = self.root
        while temp_node.positive_child is not None:
            if temp_node.data in symptoms:
                temp_node = temp_node.positive_child
            else:
                temp_node = temp_node.negative_child
        return temp_node.data

    def calculate_success_rate(self, records):
        """
        a function that calculate the success rate of the choice tree.
        :param records: a Record type records, a list of records.
        :return: the success rate of the tree.
        """
        success = 0
        for record in records:
            illness = self.diagnose(record.symptoms)
            if illness == record.illness:
                success += 1
        return success/(len(records))

    def all_illnesses(self):
        """
        a function that gives all the illnesses in the choice tree.
        using the all illnesses helper function.
        :return: a list of all the illnesses in the tree.
        """
        illness_dict = {}
        temp_root = self.root
        self.all_illnesses_helper(illness_dict, temp_root)
        # using another funtion to sort the dict.
        illness_lst = create_a_sorted_list_from_dict(illness_dict)
        # the function sorts from the lowest to the highest so i reverse it.
        illness_lst = illness_lst[::-1]
        return illness_lst

    def all_illnesses_helper(self, illness_dict, temp_root):
        """
        a function that helps finding the illnesses in the tree.
        :param illness_dict: a dictonary of the illnesses, counting
        how many times each one appeared.
        :param temp_root: a temporary root, to get in the tree.
        :return: None, but updates the illness dict.
        """
        if temp_root.positive_child is None:
            # counting how many times each one appears, and updates the dict.
            if temp_root.data in illness_dict:
                illness_dict[temp_root.data] += 1
            else:
                illness_dict[temp_root.data] = 1
            return
        self.all_illnesses_helper(illness_dict, temp_root.positive_child)
        self.all_illnesses_helper(illness_dict, temp_root.negative_child)

    def most_rare_illness(self, records):
        """
        a function that checks which illness is the most rare,
        bu checking how many times she appears.
        :param records: a list of Record type records.
        :return: the most rare illness.
        """
        illness_lst = self.all_illnesses()
        illness_dict = {}
        for record in records:
            symptoms = record.symptoms
            illness = self.diagnose(symptoms)
            # counting how many times each one appears, and updates the dict.
            if illness in illness_dict:
                illness_dict[illness] += 1
            else:
                illness_dict[illness] = 1
        # if an illness, does not appear in the tree at all, returns it.
        for flu in illness_lst:
            if flu not in illness_dict:
                return flu
        # sorting the dict, to find the most rare illness.
        illness_lst = create_a_sorted_list_from_dict(illness_dict)
        return illness_lst[0]

    def paths_to_illness(self, illness):
        """
        a function that finds the paths to a given illness.
        uses the function "path_to_illness_helper"
        :param illness: a string with a name of an illness
        :return: a list of paths to the given illness.
        """
        path_lst = []
        good_paths = []
        temp_root = self.root
        self.paths_to_illness_helper(illness, path_lst, temp_root, good_paths)
        return good_paths

    def paths_to_illness_helper(self, illness, path_lst, temp_root, good_paths):
        """
        a function that finds the paths to the illness, and updates the good_paths
        list for the main function.
        :param illness: a string of illness
        :param path_lst: a list of lists with bool expressions on them,
        True if we chose the positive child and False if we chose the positive.
        :param temp_root: a temporary root on the main tree. Node type
        :param good_paths: the paths that leads to the illness.
        :return: None, but updates the good_paths list
        """
        if temp_root.positive_child is None:
            if illness == temp_root.data:
                good_paths.append(path_lst)
            return
        self.paths_to_illness_helper(illness, path_lst + [True], temp_root.positive_child, good_paths)
        self.paths_to_illness_helper(illness, path_lst + [False], temp_root.negative_child, good_paths)


def create_a_sorted_list_from_dict(dict):
    """
    a function that creates a sorted list from a given dictonary.
    sort them from lowest to highest.
    :param dict: a dictonary to sort.
    :return: the sorted list.
    """
    sorted_by_value = sorted(dict.items(), key=lambda kv: kv[1])
    sorted_list = []
    for i in range(len(dict)):
        sorted_list.append(sorted_by_value[i][0])
    return sorted_list


def build_tree(records, symptoms):
    """
    a function that builds a binary tree, from a given records and symptoms.
    uses the build tree helper function.
    :param records: Record type records, the build the tree according to thier
    illnesses and symptoms.
    :param symptoms: a symptoms list which is each a Node part in the tree.
    :return: the root of the builded tree.
    """
    tree_root = Node(symptoms[0])
    build_tree_helper(records, symptoms, True, 0, tree_root, records[0].illness)
    return tree_root


def build_tree_helper(records, symptoms, is_symptom, index, curr_node, illness):
    """
    the function that creates the tree for the build tree function.
    the function uses recursion to build it, and builds it with the given
    records and symptoms.
    :param records: Record type records, the build the tree according to thier
    illnesses and symptoms.
    :param symptoms: a symptoms list which is each a Node part in the tree.
    :return: the root of the builded tree.
    :param is_symptom: a bool, that represent our last chose, which is True
    if we went to the positive child, and False if we went to the negative child.
    :param index: an index that we update in each recursion.
    :param curr_node: the current Node we are in.
    :param illness: a random illness, to put if we don't have any illness
    that fits in the records.
    :return: None, but builds the tree.
    """
    # each run of the recursion, we check which illnesses still fits the
    # current path. if we are on the first run (index 0) or the record list
    # is already empty, of the symptom in the list is none, we do not update.
    if (symptoms[index] is None) or (not records) or (index == 0):
        filtered_records = records
    else:
        # updates the records according to the illnesses that fits the symptoms.
        filtered_records = check_possible_records(records, symptoms[index-1], is_symptom)
    # Base case, if we reached the end of the symptom list with out indexes,
    # meaning we are on the leaf.
    if index + 1 == len(symptoms):
        # find the record that its illness fits the positive child,
        # and find the one for the negative.
        pos_illness = check_possible_records(filtered_records, symptoms[index], True)
        neg_illness = check_possible_records(filtered_records, symptoms[index], False)
        # finds the illness that fits the most, from the remaining records.
        curr_node.positive_child = Node(check_most_common_illness(pos_illness, illness))
        curr_node.negative_child = Node(check_most_common_illness(neg_illness, illness))
        return
    curr_node.positive_child = Node(symptoms[index+1])
    # go to the positive side
    build_tree_helper(filtered_records, symptoms, True, index + 1, curr_node.positive_child, illness)
    curr_node.negative_child = Node(symptoms[index+1])
    # go to the negative side.
    build_tree_helper(filtered_records, symptoms, False, index + 1, curr_node.negative_child, illness)


def check_possible_records(records, symptom, is_symptom):
    """
    a function that we use to see which records fits our current symptom.
    :param records: a list of Record type records.
    :param symptom: a symptom to see if he fits the record
    :param is_symptom: if the symptom should or should not appear in the records.
    it is a boolian expression.
    :return: the list records that fits the symptom,
    """
    filtered_records = []
    for record in records:
        # if the symptom should appear.
        if is_symptom:
            if symptom in record.symptoms:
                filtered_records.append(record)
        else:
            # if the symptom should not appear.
            if symptom not in record.symptoms:
                filtered_records.append(record)
    return filtered_records

def check_most_common_illness(records, illness):
    """
    check the illness that appears the most in the given records.
    :param records: a list of record type records
    :param illness: an illness, if we would not find a illness
    that fits the symptoms, we will return this random illness.
    :return: the illness that is the most common.
    """
    if not records:
        return illness
    illness_dict = {}
    for record in records:
        if record.illness in illness_dict:
            illness_dict[record.illness] += 1
        else:
            illness_dict[record.illness] = 1
    sorted_lst = create_a_sorted_list_from_dict(illness_dict)
    return sorted_lst[-1]


def optimal_tree(records, symptoms, depth):
    """
    a function that gets a list of records a list of symptoms and
    the depth of the tree, and creates and returns the most optimal
    tree, the tree with the biggest success rate according to the records.
    :param records: a list of record type records.
    :param symptoms: a list of symptoms.
    :param depth: the depth of the tree.
    :return: the tree with the biggest success rate.
    """
    count = 0
    opt_tree = None
    # creates all the different combinations of the symptoms.
    symptoms_comb = itertools.combinations(symptoms, depth)
    for comb in symptoms_comb:
        tree_root = build_tree(records, list(comb))
        diagnoza = Diagnoser(tree_root)
        success_rate = diagnoza.calculate_success_rate(records)
        # checks each time if the success rate is bigger than the
        # previus biggest success rate.
        if success_rate > count:
            opt_tree = tree_root
            count = success_rate
    return opt_tree

