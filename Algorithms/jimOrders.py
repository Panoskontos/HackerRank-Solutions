
def jimOrders(orders):
    serve = {}
    index = 1
    for i in orders:
        serve[index] = sum(i)
        index += 1
    # sort dictionary
    sorted_dict = {}
    sorted_keys = sorted(serve, key=serve.get)
    for w in sorted_keys:
        sorted_dict[w] = serve[w]
    return sorted_dict.keys()
