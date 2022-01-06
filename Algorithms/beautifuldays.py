def reverse_number(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


def beautifulDays(i, j, k):
    count = 0
    for x in range(i,j+1):
        reverse = reverse_number(x)
        n = abs(x-reverse)/k
        if n % 1 == 0:
            count +=1
    return count
        