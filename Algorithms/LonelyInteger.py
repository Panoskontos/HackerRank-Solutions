
def lonelyinteger(a):
    from collections import Counter
    c = Counter(a)
    for i, j in c.items():
        if j == 1:
            return i
