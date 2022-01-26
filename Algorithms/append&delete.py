def appendAndDelete(s, t, k):
    if s == t:
        return 'Yes' if k >= len(s)*2 or k % 2 == 0 else 'No'
    shorter = s if len(s) <= len(t) else t
    longer = t if len(s) <= len(t) else s
    length = len(shorter)
    min_steps = len(longer[length:])

    for i in range(length):
        if s[i] != t[i]:
            min_steps = len(s[i:]) + len(t[i:])
    return 'Yes' if (k >= len(t)*2 or (k-min_steps) % 2 == 0) and k > min_steps else 'No'
