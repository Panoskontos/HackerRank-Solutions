def taumBday(b, w, bc, wc, z):
    cost = b*bc + w*wc
    costc = cost
    # black is cheaper
    if z+bc < wc:
        costc = (b+w)*bc + z*(w)
    elif z+wc < bc:
        costc = (b+w)*wc + z*(b)

    return min(cost, costc)
