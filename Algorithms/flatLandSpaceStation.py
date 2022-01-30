def flatlandSpaceStations(n, c):
    if len(c) <= 1:
        return abs(n-len(c))
    ans = 0
    c = sorted(c)
    for i in range(1, len(c)):
        ans = max(ans, abs(c[i]-c[i-1])//2)
    return max(c[0], n-c[-1]-1, ans)
