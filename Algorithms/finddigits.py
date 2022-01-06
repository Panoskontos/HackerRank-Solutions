def findDigits(n):
    count = 0
    x = [int(a) for a in str(n)]
    for i in x:
        if i != 0 and n%i==0:
            count+=1
    return count
       