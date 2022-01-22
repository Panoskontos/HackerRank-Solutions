
def pageCount(n, p):
    x = p//2
    if n % 2 == 0:
        y = (n+1-p)//2
    else:
        y = (n-p)//2
    return min(x, y)
