def surfaceArea(array, H, W):
    M = W
    N = H
    res = 0
    for i in range(N):
        for j in range(M):
            up_side = 0
            left_side = 0
            if (i > 0):
                up_side = array[i - 1][j]
            if (j > 0):
                left_side = array[i][j - 1]
            res += abs(array[i][j] - up_side)+abs(array[i][j] - left_side)
            if (i == N - 1):
                res += array[i][j]
            if (j == M - 1):
                res += array[i][j]
    res += N * M * 2
    return res
