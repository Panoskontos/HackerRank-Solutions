def savethePrisoner(n, m, s):
    # non optimised
    # p = s
    # while m>0:
    #     p=1 if p==n else p+1
    #     m-=1
    # return n if p==1 else p-1

    # optimised
    ans = (m+s-1) % n
    if ans == 0:
        return n
    return ans
