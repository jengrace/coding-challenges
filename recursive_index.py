def recursive_index(item, lst):
    """ Given a list, return index (0-based) of item in the list.

    Return None if item is not in the list.

    """
    if item in lst:
        count = 0
        return recursive_call(item, lst, count)
    else:
        return None


def recursive_call(item, lst, count):
    if item == lst[0]:
        return count
    count = count + 1
    return recursive_call(item, lst[1:], count)


def test():
    assert recursive_index("hi", ["hey", "there", "you"]) is None
    assert recursive_index("hey", ["hey", "there", "you"]) == 0
    assert recursive_index("there", ["hey", "there", "you"]) == 1
    assert recursive_index("you", ["hey", "there", "you"]) == 2
    assert recursive_index("hey", []) is None
    print 'Tests passed'

test()
