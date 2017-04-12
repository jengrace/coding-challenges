def lemur(branches):
    """Return number of jumps needed.

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5

    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    pos = 2
    end = 0
    num_jumps = 0

    if pos == len(branches):
        num_jumps += 1
    while pos < len(branches):
        end = branches[pos]
        if end != 1:
            pos = pos + 2
            num_jumps += 1
        else:
            pos -= 1
    return num_jumps

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print