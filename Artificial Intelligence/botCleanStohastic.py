def nextMove(posr, posc, board):
    for i, j in enumerate(board):
        for k, l in enumerate(j):
            if l == 'd':
                x, y = i, k
    if posr == x and posc == y:
        print('CLEAN')
    if posr < x:
        print('DOWN')
    elif posc < y:
        print('RIGHT')
    elif posr > x:
        print('UP')
    elif posc > y:
        print('LEFT')
