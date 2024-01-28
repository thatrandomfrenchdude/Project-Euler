# # https://projecteuler.net/problem=5

def divBy(num, divBy):
    if num % divBy == 0:
        return True
    else:
        return False

def problem5_bruteForce():
    smallest_mult = 1
    while 1:
        if divBy(smallest_mult, 20) and divBy(smallest_mult, 19) and \
            divBy(smallest_mult, 19) and divBy(smallest_mult, 18) and \
            divBy(smallest_mult, 17) and divBy(smallest_mult, 16) and \
            divBy(smallest_mult, 15) and divBy(smallest_mult, 14) and \
            divBy(smallest_mult, 13) and divBy(smallest_mult, 12) and \
            divBy(smallest_mult, 11) and divBy(smallest_mult, 10) and \
            divBy(smallest_mult, 9) and divBy(smallest_mult, 8) and \
            divBy(smallest_mult, 7) and divBy(smallest_mult, 6) and \
            divBy(smallest_mult, 5) and divBy(smallest_mult, 4) and \
            divBy(smallest_mult, 3) and divBy(smallest_mult, 2):
            return smallest_mult
        smallest_mult += 1

if __name__ == '__main__':
    print('The smallest multiple is:', problem5_bruteForce())
