def sockMerchant(n, ar):
    from collections import Counter
    c = Counter(ar)
    pairs = 0
    for i in c.values():
        pairs += i//2
    return pairs
