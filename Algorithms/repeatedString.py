def repeatedString(s, n):
    return (n//len(s)) * s.count('a') + s.count('a', 0, n % len(s))
