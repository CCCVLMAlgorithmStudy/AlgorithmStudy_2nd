def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        sum = 0
        for j in range(i,n//2+2):
            sum+=j
            if sum >= n:
                break
        if sum == n:
            answer+=1
    return answer