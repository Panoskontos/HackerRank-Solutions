def gemstones(arr):
    from collections import Counter
    n = len(arr)
    c = Counter()
    for i in range(n):
        arr[i] = set(arr[i])
        c += Counter(arr[i])
    count = 0
    for i in c.values():
        if i == n:
            count += 1
    return count
