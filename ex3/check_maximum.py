from ex3 import maximum


def test():
    tests_lst = [[], [4, 4, 4], [5, 2, 1], [0], [2, 10.9, 3.3], [0, 0, 3],]
    correct_answers = [None, 4, 5, 0, 10.9, 3]
    passed = 0
    for i in range(len(tests_lst)):
        if maximum(tests_lst[i]) == correct_answers[i]:
            print('test', i + 1, 'OK')
            passed += 1
        else:
            print('test', i + 1, 'FAILED')
    if passed == 6:
        return True
    return False


if __name__ == '__main__':
    test()
