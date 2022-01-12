def maximumPerimeterTriangle(sticks):
    sticks.sort()
    d = False
    for i in range(len(sticks)-2):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            d = True
            a = sticks[i]
            b = sticks[i+1]
            c = sticks[i+2]

    if d == True:
        return [a, b, c]
    else:
        return [-1]
