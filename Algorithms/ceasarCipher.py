def caesarCipher(s, k):
    ls='abcdefghijklmnopqrstuvwxyz'
    ls=list(ls)
    a=[]
    for i in s:
        if i in ls and i.islower():
            a.append(ls[(ls.index(i)+k)%26])
        elif i.lower() in ls and i.isupper():
            a.append(ls[(ls.index(i.lower())+k)%26].upper())
        else:
            a.append(i)
    # join list of strings in a single string 
    return (''.join(a))

    