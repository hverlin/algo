def primality_test(N):
    """Return True if N is prime, False otherwise.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> primality_test(1)
    False
    >>> primality_test(2)
    True
    >>> primality_test(1162202581)
    False
    >>> primality_test(3317044064679887385961981)
    False
    """

    def witness_loop(n, a):
        print(a)
        # write n − 1 as d.2^r with d odd by factoring powers of 2 from n − 1
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1

        if (a ** d % n) == 1:
            return False

        for i in range(s):
            print(i, s)
            if (a ** (2 ** i * d) % n) == n - 1:
                return False

        return True

    def maybe_prime(n):

        if n in primes or n == 0:
            return True

        if n == 1 or any((n % p) == 0 for p in primes):
            return False

        return not any(witness_loop(n, a) for a in primes)

    primes = [2, 3]
    primes += [x for x in range(5, 2000, 2) if maybe_prime(x)]

    return maybe_prime(N)
