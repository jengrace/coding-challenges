def sum_list(nums):
    """Using recursion, return the sum of numbers in a list.

    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

    >>> sum_list([])
    0

    """

    if len(nums) == 0:
        return 0
    return sum_list(nums[1:]) + nums[0]


#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print