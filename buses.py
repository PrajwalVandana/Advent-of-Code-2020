import functools
import math

# a module with a bunch of functions I wrote
# https://github.com/PrajwalVandana/Shortcuts
from mymodules import shortcuts as sh


def mod_inv(n, div):
    """Returns the modular inverse of n mod div."""
    if math.gcd(n, div) != 1:
        return None
    else:
        return pow(n, sh.phi(div)-1, div)  # sh.phi finds phi(n)


def solve_mod_equations(*args):
    """Solves a system of modular congruences, where each argument is a tuple of the
    form ```(a, p)```. In this case, x == a (mod p).

    Returns a tuple ```(b, q)```, where x == b (mod q) is the general solution \
    of the system."""
    def solve_mod_equation(t1, t2):
        t1, t2 = sorted((t1, t2), key=lambda x: x[1])
        a, p, b, q = t1+t2
        return (q*mod_inv(q, p)*(a-b) + b) % (q*p), q*p

    return functools.reduce(lambda res, div: solve_mod_equation(res, div), args)


with open('/users/sysadmin/Documents/Prajwal/Programming/Python/Competitions/Advent of Code/input.txt') as fin:
    fin.readline()

    eqns = list(map(lambda tup: (-tup[0], int(tup[1])), filter(
        lambda x: x[1] != 'x', enumerate(fin.readline().strip().split(',')))))

    print((res := solve_mod_equations(*eqns)[0]))
