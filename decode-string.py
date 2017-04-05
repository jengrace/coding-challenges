def decode(s):
    """Decode a string.

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'

    """

    decoded_str = []
    for e in s:
        if e.isdigit():
            pos_to_skip = int(e)
        elif pos_to_skip > 0:
            pos_to_skip -= 1
        else:
            decoded_str.append(e)
    return ''.join(decoded_str)

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
