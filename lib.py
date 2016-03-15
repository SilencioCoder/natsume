import math


def fib(n, start1=1, start2=2):
    yield start1
    a, b = start1, start2
    while b < n:
        yield b
        a, b = b, a + b


def is_prime(n, prime_list=None):
    if prime_list is None:
        pass


def primes(n):
    numbers = {p: None for p in range(2, n+1)}

    for p in range(2, n+1):
        if numbers[p] is None:
            numbers[p] = True
            yield p
            for c in range(p*p, n+1, p):
                numbers[c] = False
        if p*p > n:
            break

def primes_x(n):
    numbers = {p: True for p in range(2, n+1)}

    for p in range(2, n+1):
        for c in range(p*p, n+1, p):
            numbers[c] = False

    return [p for p in range(2, n+1) if numbers[p]]
