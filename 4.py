# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import math


def checkPalindrome(num):
    val = str(num)
    for i in range(0, math.floor(len(val)/2)):
        if val[i] != val[len(val) - 1 - i]:
            return False
    return True


def problem4():
    max_palindrome = 0
    for i in range(100, 999):
        for j in range(100, 999):
            mult_val = i * j
            if checkPalindrome(mult_val) and mult_val > max_palindrome:
                max_palindrome = mult_val
    print('The max palindrome is:', max_palindrome)


if __name__ == '__main__':
    problem4()
