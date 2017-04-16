# If the word begins with a consonant (not a, e, i, o, u), move the first
# letter to the end and add 'ay'

# If the word begins with a vowel, add 'yay' to the end


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'

    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    l = list(phrase)
    s = ''
    words = []
    space = 0
    beg = 0
    pig_lat = ''
    for pos in range(len(phrase)):
        if l[pos] == ' ':
            space = pos
            words.append(l[beg:space])
            beg = space + 1
    words.append(l[beg:])

    for i, e in enumerate(words):
        first_letter = e[0]
        if first_letter not in vowels:
            new_word = e[1:]
            first_letter = first_letter+'ay'
            new_word.append(first_letter)
            if i == len(words)-1:
                s = ''.join(new_word)
            else:
                s = ''.join(new_word) + ' '
            pig_lat = pig_lat + s

        elif first_letter in vowels:
            last_letter = e[-1]
            new_word = e[:-1]
            last_letter = last_letter + 'yay'
            new_word.append(last_letter)
            if i == len(words)-1:
                s = ''.join(new_word)
            else:
                s = ''.join(new_word) + ' '
            pig_lat = pig_lat + s

    return pig_lat

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print