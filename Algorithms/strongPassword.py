def minimumNumber(n, password):
    missing = 0
    # has digit
    has_digit = False
    for i in password:
        if i.isdigit():
            has_digit = True
    if has_digit == False:
        missing += 1
    # has upper
    has_upper = False
    for i in password:
        if i.isupper():
            has_upper = True
    if has_upper == False:
        missing += 1
    # has lower
    has_lower = False
    for i in password:
        if i.islower():
            has_lower = True
    if has_lower == False:
        missing += 1
    # has special char
    special_chars = '!@#$%^&*()-+'
    has_special = False
    for i in password:
        if i in special_chars:
            has_special = True
    if has_special == False:
        missing += 1

    return max(missing, 6-n)
