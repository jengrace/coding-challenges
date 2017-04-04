def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    """
    splits = []
    beg = 0
    end = 0
    for pos in range(len(astring)):
        if pos+len(splitter) <= len(astring):
            if astring[pos:pos+len(splitter)] == splitter:
                end = pos
                word = astring[beg:end]
                splits.append(word)
                beg = pos+len(splitter)
            else:
                end = pos
    splits.append(astring[beg:])
    return splits

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print