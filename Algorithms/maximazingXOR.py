def maximizingXor(l, r):
    return max(max(i ^ r, i ^ l) for i in range(l, r))
