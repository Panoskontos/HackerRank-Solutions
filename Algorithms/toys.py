def toys(w):
    w.sort()
    c = 1
    base = w[0]+4
    for i in range(len(w)):
        if w[i] > base:
            c += 1
            base = w[i] + 4
    return c
