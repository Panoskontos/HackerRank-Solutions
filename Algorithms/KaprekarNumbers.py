def checkIsKaprekar(num):
    if(num == 1):
        return True
    elif((num**2) < 15):
        return False
    string_num = str(num**2)
    if num == int(string_num[:len(string_num)//2]) + int(string_num[len(string_num)//2:]):
        return True


def kaprekarNumbers(start, end):
    numbers = []
    for i in range(start, end+1):
        if checkIsKaprekar(i):
            numbers.append(i)
    if numbers:
        for i in numbers:
            print(i, end=' ')
    else:
        print('INVALID RANGE')
