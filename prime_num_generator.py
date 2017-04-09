def primes(count):
    """Return count number of prime numbers, starting at 2.

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    """
    prime_nums = []
    i = 2
    while len(prime_nums) < count:
        if is_prime(i) is True:
            prime_nums.append(i)
        i = i + 1
    return prime_nums


def is_prime(num):
    if num == 2:
        return True
    if num % 2 != 0:  # analyze only the odd nums
        i = num/2
        keep_trying = True
        while i > 1 and keep_trying is True:
            if num % i == 0:
                keep_trying = False
            i -= 1
        if keep_trying is True:
            return True


#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
