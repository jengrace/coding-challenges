def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

    >>> lst = [1, 2, 3, 4, 6, 8]

    >>> show_evens(lst)
    [1, 3, 4, 5]

    """
    even_nums_indices = []
    count = 0
    for num in nums:
        if num % 2 == 0:
            even_nums_indices.append(count)
        count += 1
    return even_nums_indices

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
