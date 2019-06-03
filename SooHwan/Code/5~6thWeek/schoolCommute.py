def solution(m, n, puddles):
    graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
    path = [[0 for _ in range(m+1)] for _ in range(n+1)]
    path[1][1] = 1
    for p in puddles:
        graph[p[1]][p[0]] = -1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if graph[i][j] == -1:
                path[i][j] = 0
            else:
                path[i][j] += path[i-1][j] + path[i][j-1]
                path[i][j] %= 1_000_000_007

    return path[n][m]