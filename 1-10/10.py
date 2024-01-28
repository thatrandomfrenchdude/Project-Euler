import math

# # https://projecteuler.net/problem=10

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


def problem10():
    prime_sum = 0
    for n in range(2000000):
        if is_prime(n):
            prime_sum += n
    print('The sum of primes under 2 million is', prime_sum)


if __name__ == '__main__':
    problem10()
