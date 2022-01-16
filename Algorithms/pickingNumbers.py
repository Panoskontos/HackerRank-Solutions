def pickingNumbers(a):
    a.sort()
    from collections import Counter
    c = Counter(a)
    print(c)
    sub = []
    for i in range(1, len(a)):
        if a[i-1] + 1 == a[i]:
            sub.append(c[a[i-1]] + c[a[i]])

    for i in range(1, len(a)):
        if a[i-1] == a[i]:
            sub.append(c[a[i-1]])

    if len(sub) == 0:
        return len(a)
    else:
        return max(sub)
