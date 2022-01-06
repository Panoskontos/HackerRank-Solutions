
def marsExploration(s):
    c=0
    for i in range(0,len(s),3):
            if (not (s[i:i+3]=="SOS")):
                
                if s[i] != "S":
                    c+=1
                if s[i+1] != "O":
                    c+=1
                if s[i+2] != "S":
                    c+=1
            
    return c

    