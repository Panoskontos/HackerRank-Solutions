def howManyGames(p, d, m, s):
    games = 0
    if s < p:
        return 0
    s = s-p
    games += 1
    while s >= m and s >= p:
        p = p-d
        if p <= m:
            s = s - m
            games += 1
        else:
            s = s - p
            games += 1
    return games
