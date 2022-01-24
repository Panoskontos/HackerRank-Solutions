def bfs(n, m, edges, s):
    import queue

    result = [-1] * n
    result[s - 1] = 0
    neighbors = []
    for i in range(n):
        neighbors.append(set())
    for e in edges:
        neighbors[e[0] - 1].add(e[1])
        neighbors[e[1] - 1].add(e[0])
    q = queue.Queue()
    q.put(s)
    while q.qsize() > 0:
        node = q.get()
        for neighbor in neighbors[node - 1]:
            if result[neighbor - 1] == -1:
                result[neighbor - 1] = result[node - 1] + 6
                q.put(neighbor)
    result.pop(s - 1)
    return result
