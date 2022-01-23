def nextMove(n, r, c, grid):
    m_x, m_y = r, c
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p_x, p_y = i, j

    if p_x > m_x:
        return "DOWN"
    elif p_x < m_x:
        return 'UP'
    elif p_y < m_y:
        return 'LEFT'
    elif p_y > m_y:
        return 'RIGHT'
