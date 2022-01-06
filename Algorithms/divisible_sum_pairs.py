def divisibleSumPairs(n, k, ar):
    count = 0 
    for i in range(len(ar)):
        for j  in range(1,len(ar)):
            if i<j:
                if (ar[i]+ar[j])%k==0:
                    count+=1
    return count
