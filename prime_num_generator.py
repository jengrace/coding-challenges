def primes(count):
    """Return count number of prime numbers, starting at 2.

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    """

    # prime_nums = []
    # i = 0

    # while i < count:
    #     print i
    #     i += 1

    # a number is prime only if it divisible by itself and 1

    n = 3
    odd_nums = []
    while n < 20:
        if n % 2 != 0:
            odd_nums.append(n)
        n += 1
    for num in odd_nums:
        print num

primes(5)
#####################################################################

# if __name__ == "__main__":
#     import doctest

#     print
#     result = doctest.testmod()
#     if not result.failed:
#         print "ALL TESTS PASSED. GOOD WORK!"
#     print