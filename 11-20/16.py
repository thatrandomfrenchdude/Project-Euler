# 2^15 = 32768 adn the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# what is the sum of the digits of the number 2^1000?

def problem16() -> int:
    return sum([int(i) for i in str(2 ** 1000)])

if __name__ == '__main__':
    print(problem16())