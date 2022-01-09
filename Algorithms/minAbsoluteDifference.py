def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    n = len(arr)
    diff = 1000000
    for i in range(1, n):
        if diff > abs(arr[i-1]-arr[i]):
            diff = abs(arr[i-1]-arr[i])
    return diff
