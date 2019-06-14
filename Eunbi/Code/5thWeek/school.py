def solution(m, n, puddles):
    dp = []

    for i in range(0, n):
        dp.append([])
        for j in range(0, m):
            dp[i].append(1)

    for i in puddles: 
        dp[i[1]-1][i[0]-1] = 0

    for i in range(0, m):
        if dp[0][i] == 0:
            for j in range(i, m):
                dp[0][j] = 0

    for i in range(0, n): 
        if dp[i][0] == 0:
            for j in range(i, n):
                dp[j][0] = 0

    for i in range(1, n): 
        for j in range(1, m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
    answer = dp[n-1][m-1] % 1000000007
                
    return answer