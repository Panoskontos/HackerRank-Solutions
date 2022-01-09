
def missingNumbers(arr, brr):
    from collections import Counter
    c1 = Counter(arr)
    c2 = Counter(brr)
    union = c1 | c2
    inter = c1 & c2
    diff = union - inter
    return sorted(diff.keys())
    # elegant solution
