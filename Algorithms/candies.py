def candies(n, arr):
    # create empty array of 1,1,1,1,1
    c = [1]*n

    # left to right
    for i in range(n-1):
        # if bigger than next, candies[i] = candies[next]+1
        if arr[i] > arr[i+1]:
            c[i] = max(1 + c[i+1], c[i])
        # if smaller than next, candies[next] = candies[i]+1
        elif arr[i+1] > arr[i]:
            c[i+1] = max(1 + c[i], c[i+1])

    # right to left
    for i in range(n-1, 0, -1):
        # if bigger than previous, candies[i] = candies[prev]-1
        if arr[i] > arr[i-1]:
            c[i] = max(1 + c[i-1], c[i])
        # if smaller than previous, candies[prev] = candies[i]-1
        elif arr[i-1] > arr[i]:
            c[i-1] = max(1 + c[i], c[i-1])

    return sum(c)
