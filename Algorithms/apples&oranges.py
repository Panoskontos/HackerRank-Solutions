def countApplesAndOranges(s, t, a, b, apples, oranges):
    sam_apples = 0
    for i in apples:
        if (i + a) >= s and (i + a)<= t:
            sam_apples+=1
    print(sam_apples)
    sam_oranges = 0
    for i in oranges:
        if (b + i) >= s and (i + b)<= t:
            sam_oranges+=1
    print(sam_oranges)


