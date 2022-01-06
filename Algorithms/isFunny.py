def isFunny(s):
    for i in range(1, len(s)):
        if abs(s[i] - s[i-1]) != abs(s[-i-1] - s[-i]): return False
    return True