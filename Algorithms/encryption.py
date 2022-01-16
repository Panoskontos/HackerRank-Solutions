import math


def encryption(s):
    s.strip()
    row, col, res = math.floor(
        math.sqrt(len(s))), math.ceil(math.sqrt(len(s))), ''
    for i in range(col):
        for j in range(i, len(s), col):
            res += s[j]
        res += ' '
    return res
