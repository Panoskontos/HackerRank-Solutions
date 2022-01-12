def maximumToys(prices, k):
    prices.sort()
    i = 0
    while k > 0:
        k -= prices[i]
        i += 1
    return i-1
