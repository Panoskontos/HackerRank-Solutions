
def beautifulTriplets(d, c):
    gc = 0
    n = len(c)
    for i in range(n):
        if c[i]+d in c and c[i]+2*d in c:
            gc += 1
    return gc
