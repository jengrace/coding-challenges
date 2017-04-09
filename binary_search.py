def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7

    """
    # l = [] # list of number of guesses
    # for i in range(1,101):
    #     l.append(binary_search(i)) # number of guesses
    #  return max(l)

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    guess = 50
    low = 0
    high = 100

    while guess != val:
        if guess > val:
            high = guess
            guess = round((high + low)/2)
            num_guesses += 1
        if guess < val:
            low = guess
            guess = round((high + low)/2)
            num_guesses += 1

    if guess == val:
        num_guesses += 1

    return num_guesses

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print