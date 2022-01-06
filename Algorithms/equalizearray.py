def equalizeArray(arr):
    frequency = []
    for i in arr:
        frequency.append(arr.count(i))
    top_num = max(frequency)
    return len(arr) - top_num