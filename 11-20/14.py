def sequence(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def problem14():
    res = 0
    max_length = 0

    for i in range(1, 1000000):
        length = 1
        n = i
        while n != 1:
            n = sequence(n)
            length += 1
        if length > max_length:
            max_length = length
            res = i
    
    return res

if __name__ == '__main__':
    print(problem14())