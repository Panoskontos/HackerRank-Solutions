def next_move(posr, posc, board):
    dirt = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                dirt.append([i, j])
    if posr == dirt[0][0] and posc == dirt[0][1]:
        print('CLEAN')
    elif posc < dirt[0][1]:
        print('RIGHT')
    elif posc > dirt[0][1]:
        print('LEFT')
    elif posr < dirt[0][0]:
        print('DOWN')
