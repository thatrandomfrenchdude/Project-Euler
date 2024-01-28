# Using names.txt, a 46K text file containing over
# five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical
# value for each name, multiply this value by its
# alphabetical position in the list to obtain a name
# score.

# For example, when the list is sorted into alphabetical
# order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain
# a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calc_name_score(name: str) -> int:
    return sum([ALPHABET.index(c) + 1 for c in name])

def readFile(path: str) -> list:
    with open(path, 'r') as f:
        return f.read().replace("\"", "").split(',')

def problem22() -> int:
    names = sorted(readFile('assets/0022_names.txt'))
    names_len = len(names)

    names_sum = 0

    # ensure colin is 938th
    assert names[937] == 'COLIN'

    for i in range(names_len):
        names_sum += calc_name_score(names[i]) * (i + 1)

    return names_sum

if __name__ == '__main__':
    print(problem22())
