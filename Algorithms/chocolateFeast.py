def chocolateFeast(n, c, m):
    if c > n:
        return 0
    wrappers = n//c
    amount = wrappers
    while wrappers >= m:
        wrappers -= m
        wrappers += 1
        amount += 1
    return amount
