# # https://projecteuler.net/problem=2

def problem2():
    sum = 0
    first = 1
    second = 2
    while second < 4000000:
        if second % 2 == 0:
            sum += second
        temp = second
        second += first
        first = temp
    return sum

print(problem2())
