def icecreamParlor(m, arr):
    n = len(arr)
    indexes = []
    for i in range(n):
        for j in range(n):
            if (arr[i]+arr[j] == m and i != j):
                return i+1, j+1
