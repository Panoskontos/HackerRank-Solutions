
def marcsCakewalk(calorie):
    n = len(calorie)
    calorie.sort(reverse=True)
    miles = 0
    for i in range(n):
        miles += (2**i)*calorie[i]
    return miles
