
def fairRations(B):
    count = 0
    for i in range(len(B)-1):
        if B[i]%2==1:
            B[i]+=1            
            B[i+1]+=1
            count +=2 
    for i in B:
        if i%2!=0:
            return 'NO'           
    return str(count)
         
        