
def countingSort(arr):
    from collections import Counter
    frequences = [0] * 100
    for i in range(100):
        for j in arr:
            if i == j:
                frequences[i] += 1
    return frequences
