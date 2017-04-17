def print_recursively(lst):
    """Print items in the list, using recursion.

    >>> print_recursively([1, 2, 3])
    1
    2
    3

    """

    if len(lst) != 0:
        print lst[0]
        print_recursively(lst[1:])


#####################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
