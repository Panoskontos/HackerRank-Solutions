
def separateNumbers(s):
    for i in range(len(s)//2):
        # grab first digits
        a = s[0:i+1]
        # empty string
        b = ""
        # make int
        c = int(a)
        # add to string
        b = b+a
        while True:
            # add 1
            c = c+1
            # create str + str+1
            b = b+str(c)
            # until you have created a string
            if len(b) >= len(s):
                break
        # if str is identical
        if b == s:
            print("YES", a)
            return
    print("NO")
