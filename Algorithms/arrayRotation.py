def circularArrayRotation(a, k, queries):
    # non optimised solution for half the tests
    # if k%len(a)==0:
    #     return list(a[i] for i in queries)
    # for i in range(k):
    #     a= a[k:] + a[:k]
    # return list(a[i] for i in queries)

    # faster solution
    while(k):
        k = k-1
        # faster rotation
        a.insert(0, a.pop())

    return [a[i] for i in queries]
