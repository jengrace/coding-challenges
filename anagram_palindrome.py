def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

    """

    count = 0
    char_counter = {}
    for letter in word:
        if letter in char_counter:
                char_counter[letter] += 1
        else:
            char_counter[letter] = 1

    for k in char_counter:
        if len(word) % 2 == 0:
            if char_counter[k] % 2 != 0:
                return False
        else:
            if char_counter[k] % 2 != 0:
                count += 1
    if count == 1:
        return True
    return True

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print