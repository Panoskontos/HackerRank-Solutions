
def closestNumbers(arr):
    arr = sorted(arr)
    n = len(arr)
    diff = 1000000
    for i in range(1, n):
        if diff > abs(arr[i-1]-arr[i]):
            diff = abs(arr[i-1]-arr[i])

    chosen = []
    for i in range(1, n):
        if abs(arr[i-1] - arr[i]) == diff:
            chosen.append(arr[i-1])
            chosen.append(arr[i])
    return chosen
