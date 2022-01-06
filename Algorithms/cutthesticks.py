def cutTheSticks(arr):
    
    numberofsticks = []
    
    while arr:
        numberofsticks.append(len(arr))
        
        shortest = min(arr)
          
        arr= [i for i in arr if i!=shortest]
            
    return numberofsticks

    