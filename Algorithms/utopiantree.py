
def utopianTree(n):
    if n == 0:
        return 1
    elif n==1:
        return 2
    else:
        height = 2
        for i in range(2,n + 1):
            if i%2==0:
                height += 1
            else:
                height *= 2
        return height
    