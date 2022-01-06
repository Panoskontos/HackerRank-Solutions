# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    mouse = z
    cat1 = x
    cat2 = y
    if abs(cat1-mouse) > abs(mouse - cat2):
        return 'Cat B'
    elif abs(cat1-mouse) == abs(mouse - cat2):
        return 'Mouse C'
    else:
        return 'Cat A'
    