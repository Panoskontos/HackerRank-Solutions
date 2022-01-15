def maxMin(k, arr):
    n = len(arr)
    arr.sort()
    ae = 999999999
    for i in range(n-k+1):
        v = abs(arr[i]-arr[i+k-1])
        if v < ae:
            ae = v
    return ae
