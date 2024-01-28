# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a =/= b, then a and b
# are an amicable pair and each of a and b are called
# amicable numbers.

# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore $d(220) = 284$. The proper divisors of 284
#  are $1, 2, 4, 71$ and $142$; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# how speed this up?
def calc_divisors(n: int) -> list:
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def check_amicable(a, b, memo) -> bool:
    if a in memo:
        divisors_a = memo[a]
    else:
        divisors_a = calc_divisors(a)
        memo[a] = divisors_a

    if b in memo:
        divisors_b = memo[b]
    else:
        divisors_b = calc_divisors(b)
        memo[b] = divisors_b

    return sum(divisors_a) == b and sum(divisors_b) == a

def problem21() -> int:
    memo_divisors = {}
    amicable_set = set()

    for i in range(1, 10001):
        for j in range(1, 10001):
            if i == j:
                continue
            if check_amicable(i, j, memo_divisors):
                amicable_set.add(i)
                amicable_set.add(j)
    
    return sum(amicable_set)


if __name__ == '__main__':
    print(problem21())
