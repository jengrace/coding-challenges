def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise.

        >>> is_pangram("The quick brown fox jumps over the lazy dog!")
        True

        >>> is_pangram("I like cats, but not mice")
        False

    """
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z'])

    for letter in sentence:
        if letter in alphabet:
            alphabet.remove(letter)
    if len(alphabet) == 0:
        return True
    return False

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
