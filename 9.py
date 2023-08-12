# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2. For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def isPythTriple(a, b, c):
    if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
        return True
    return False


def problem9():
    a = 1
    while a < 1000:
        b = a + 1
        while a + b < 1000:
            c = b + 1
            while a + b + c <= 1000:
                if a + b + c == 1000 and isPythTriple(a, b, c):
                    return a, b, c
                c += 1
            b += 1
        a += 1


if __name__ == '__main__':
    print('Running...')
    a, b, c = problem9()
    print('A =', a)
    print('B =', b)
    print('C =', c)
    print('The product is:', a * b * c)
    print('Check:', a + b + c)
