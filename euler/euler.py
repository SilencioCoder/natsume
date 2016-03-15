from lib import *


def p1():
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)


def p2():
    return sum(i for i in fib(4000000) if i % 2 == 0)
