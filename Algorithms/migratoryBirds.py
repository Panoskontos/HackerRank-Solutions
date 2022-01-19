
def migratoryBirds(arr):
    from collections import Counter
    c = Counter(arr)
    biggest = []
    for i, j in c.items():
        if j == max(c.values()):
            biggest.append(i)
    return (biggest[0] if len(biggest) == 1 else min(biggest))
