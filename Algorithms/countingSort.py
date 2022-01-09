
def countingSort(arr):
    # frequency table
    frequences = [0] * 100
    for i in range(100):
        for j in arr:
            if i == j:
                frequences[i] += 1

    # result table
    result = []
    for i in range(100):
        for j in range(frequences[i]):
            result.append(i)
    return result
