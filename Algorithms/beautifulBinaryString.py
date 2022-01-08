
def beautifulBinaryString(b):
    b = list(b)
    n = len(b)
    count = 0
    for i in range(0, n-2):
        if b[i] == '0' and b[i+1] == '1' and b[i+2] == '0':
            count += 1
            b[i+2] = '1'
    if count == 0:
        return 0
    return count
