import math

# # https://projecteuler.net/problem=6

def problem6():
    sum_squares = 0
    square_sum = 0

    for number in range(1, 101):
        sum_squares += math.pow(number, 2)
        square_sum += number

    print('The answer to problem 6 is:', math.pow(square_sum, 2) - sum_squares)


if __name__ == '__main__':
    problem6()
