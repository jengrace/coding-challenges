def deduped(items):
    """Return new list from items with duplicates removed.
    >>> deduped([1, 1, 1])
    [1]

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> deduped([1, 2, 3])
    [1, 2, 3]

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

    >>> deduped([])
    []

    """

    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
