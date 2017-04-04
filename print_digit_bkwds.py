def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.

    >>> print_digits(1)
    1
    >>> print_digits(314)
    4
    1
    3
    >>> print_digits(12)
    2
    1

    """

    while num > 0:
        next_digit = num % 10
        print next_digit
        num = (num - next_digit) / 10

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print