
def minimumDistances(a):
    distances = []
    for i in range(len(a)):
        for j in reversed(range(len(a))):
            if i==j:
                break
            if a[i]==a[j]:
                distances.append(j-i)
                
    if distances:
        return min(distances)
    else:
        return -1         
    
   