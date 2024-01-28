# https://projecteuler.net/problem=1

# sum of multiples of a and b below limit
# generalized solution for problem 1
def sum_of_multiples(a, b, limit):
    sum = 0
    for i in range(limit):
        if i % a == 0 or i % b == 0:
            sum += i
    return sum

# example: sum of multiples of 3 and 5 below 1000
def problem1():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

if __name__ == '__main__':
    print(problem1())
