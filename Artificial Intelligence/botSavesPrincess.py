# slower code for 1/3
def displayPathtoPrincess(n, grid):
    for i in range(n):
        for k in range(n):
            if grid[i][k] == 'm':
                m_x, m_y = k, i
            if grid[i][k] == 'p':
                p_x, p_y = k, i

    h, v = abs(p_x - m_x), abs(p_y - m_y)
    if p_x > m_x:
        print("RIGHT" * h)
    elif p_x < m_x:
        print("LEFT" * h)
    if p_y > m_y:
        print("DOWN" * v)
    elif p_y < m_y:
        print("UP" * v)

# The faster code that won 3/3
# we always start at middle
# princes always at a corner


def displayPathtoPrincess(n, grid):
    if grid[0][0] == 'p':
        print('UP\nLEFT\n' * ((n-1)//2))
    elif grid[n-1][0] == 'p':
        print('DOWN\nLEFT\n' * ((n-1)//2))
    elif grid[0][n-1] == 'p':
        print('UP\nRIGHT\n' * ((n-1)//2))
    elif grid[n-1][n-1] == 'p':
        print('DOWN\nRIGHT\n' * ((n-1)//2))
