def hackerrankInString(s):

    target = list('hackerrank')

    for c in s:
        if c == target[0]:
            target.pop(0)
        if len(target) == 0:
            return 'YES'

    return 'NO'
