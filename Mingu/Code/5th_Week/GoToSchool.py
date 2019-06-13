# def notpuddles(puddles,now):
#     rtn = True
#     for i in puddles:
#         if i == now:
#             rtn = False
#             break;
#     return rtn

def solution(m, n, puddles):
    matrix = [[0 for col in range(101)] for row in range(101)]
    # now_n = now_m = 1
    matrix[1][1] = 1
    for j in range(1,n+1):
        for i in range(1,m+1):
            if [i,j] not in puddles:
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]
                # print(matrix[i][j])
    return matrix[m][j]%1000000007

# def solution(m, n, puddles):
#     answer = 0
#     stack = [[1,1]]
#     while stack:
#         tmp = stack.pop()
#         #학교인지 확인
#         if tmp == [m,n]:
#             answer+=1
#         else:
#             #우측으로
#             # if notpuddles(puddles,[tmp[0]+1,tmp[1]]) and tmp[0]<m:
#             if [tmp[0]+1,tmp[1]] not in puddles and tmp[0]<m:
#                 stack.append([tmp[0]+1,tmp[1]])
#             #아래로
#             if [tmp[0],tmp[1]+1] not in puddles and tmp[1]<n:
#                 stack.append([tmp[0],tmp[1]+1])
        
#     # print(stack)
#     return answer