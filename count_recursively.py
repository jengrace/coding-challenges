'''Count the number of items in a list, using recursion.'''


def count_recursively(lst):
    if lst:
        return count_recursively(lst[1:]) + 1
    else:
        return 0


def test():
    assert count_recursively([1, 2, 3, 4]) == 4
    assert count_recursively([1]) == 1
    assert count_recursively([1, 2, 3, 4, 5]) == 5
    assert count_recursively([1, 2, 3, 4]) == 4
    assert count_recursively(['abc', 'a', 'b', 'c']) == 4
    assert count_recursively([]) == 0
    assert count_recursively([[1, 2, 3], [2], [9]]) == 3
    print 'Tests passed'

test()
