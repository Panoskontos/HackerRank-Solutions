import math

def viralAdvertising(n):
    shares = 5
    total_likes = 2
    if n==1:
        return 2
    likes = 2
    for i in range(1,n):
        shares = likes * 3
        likes = math.floor(shares/2)
        total_likes += likes
    return total_likes
        