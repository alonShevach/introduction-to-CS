from largest_and_smallest import largest_and_smallest


def test_largest_and_smallest():
    """function that tests the function largest_and_smallest for problems"""
    max_test, min_test = largest_and_smallest(0, 0, 0)
    max_test2, min_test2 = largest_and_smallest(-1, 10, -13.2)
    max_test3, min_test3 = largest_and_smallest(5, -20, 5)
    max_test4, min_test4 = largest_and_smallest(10.5, 20, 133.337)
    max_test5, min_test5 = largest_and_smallest(90, -50, -50)
    if ((max_test == 0) and (min_test == 0)) or ((max_test2 == 10) and (min_test2 == -1)) or \
    ((max_test3 == 5) and (min_test3 == -20)) or ((max_test4 == 133.337) and (min_test4 == 10.5)) or \
    ((max_test5 == 90) and (min_test5 == -50)):
        return True
    return False


if __name__ == "__main__":
    test_largest_and_smallest()
