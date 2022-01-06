def makingAnagrams(s1, s2):
    from collections import Counter
    dict1 = Counter(s1)
    dict2 = Counter(s2)
    return (sum((dict1-dict2).values())) + (sum((dict2-dict1).values()))
    