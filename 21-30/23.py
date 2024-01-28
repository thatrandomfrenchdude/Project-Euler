# A perfect number is a number for which the sum of its
# proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
# is a perfect number.

# A number n is called deficient if the sum of its
# proper divisors is less than n and it is called
# abundant if this sum exceeds n.

# As 12 is the smallest abundant number,
# 1 + 2 + 3 + 4 + 6 = 16, the smallest number
# that can be written as the sum of two
# abundant numbers is 24.

# By mathematical analysis,
# it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any
# further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of
# two abundant numbers is less than this limit.

# Find the sum of all the positive integers which
# cannot be written as the sum of two abundant numbers.

def calc_divisors(n: int) -> list:
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_abundant(n: int, memo: dict) -> bool:
    divisors = calc_divisors(n)
    memo[n] = sum(divisors) > n
    return memo[n]

def problem23() -> int:
    result = 0
    memo = {}
    
    for i in range(1, 28124):
        val = False

        for j in range(1, i):
            a = memo[j] if j in memo else is_abundant(j, memo)
            b = memo[i - j] if i - j in memo else is_abundant(i - j, memo)
            
            if a and b:
                val = True
                break

        if not val:
            result += i
    
    return result

if __name__ == '__main__':
    print(problem23())