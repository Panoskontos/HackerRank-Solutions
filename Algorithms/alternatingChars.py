def alternatingCharacters(s):
    if len(set(s))==1:
        return len(s)-1
    
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c+=1
    return c
      