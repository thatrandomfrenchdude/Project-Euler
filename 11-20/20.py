# n! means n x (n - 1) x ... x 3 x 2 x 1

# for example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# find the sum of the digits in 100!

def problem20() -> int:
    from math import factorial
    return sum([int(i) for i in str(factorial(100))])

if __name__ == '__main__':
    print(problem20())