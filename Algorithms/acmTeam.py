def acmTeam(topic):
    from itertools import combinations
    from collections import Counter

    s = map(lambda x: int(x, 2), topic)
    u = Counter(bin(a | b).count('1') for a, b in combinations(s, 2))
    w = max(u.keys())
    return [w, u[w]]
