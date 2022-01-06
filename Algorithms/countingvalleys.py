
def countingValleys(steps, path):
    total = 0 
    valley = 0
    for i in path:
        if i =='D':
            total -=1
        else:
            total +=1
            if total==0:
                valley+=1
            
    return valley