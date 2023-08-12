# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(math.pow(n, 0.5))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def problem7():
    prime_count = 0
    num = 1

    while prime_count != 10001:
        num += 1
        if is_prime(num):
            prime_count += 1
            print('prime', prime_count, ':', num)
    print('The 10001st prime is:', num)


if __name__ == '__main__':
    problem7()
