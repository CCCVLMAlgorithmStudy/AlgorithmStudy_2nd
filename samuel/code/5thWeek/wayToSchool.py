def solution(m, n, puddles):
    arr = [[0]*m for i in range(n)]
    for i in range(len(puddles)) :
        arr[puddles[i][1]-1][puddles[i][0]-1] = -1
    for i in range(0,n) :
        for j in range(0,m) :
            if ((i == 0 and j == 1) or (i == 1 and j == 0)) and arr[i][j] != -1 :
                arr[i][j] = 1
                continue
            if arr[i][j] == -1 or (arr[i][j-1] == -1 and arr[i-1][j] == -1) :
                arr[i][j] = 0
            elif arr[i][j-1] == -1 :
                arr[i][j] = arr[i-1][j]
            elif arr[i-1][j] == -1 :
                arr[i][j] = arr[i][j-1]
            else :
                arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000007
    return arr[i][j]