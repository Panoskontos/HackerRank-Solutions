def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i<(len(c)-1):
        if (i < len(c)-2) and c[i+2]==0:
            jumps+=1
            i+=2
        elif c[i+1] ==0:
            jumps+=1
            i+=1
    return jumps
