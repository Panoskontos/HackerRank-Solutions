
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        # j = previous
        j = i - 1
        while j >= 0 and key < arr[j]:
            # if key is less than previous move back
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

        str = ''
        for i in arr:
            str += f'{i} '
        print(str)
