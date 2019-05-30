def solution(n):
    num = n//2+1
    answer = 1
    for i in range(1,num+1):
        temp = i
        compare = i
        while compare<n:
            temp += 1
            compare += temp
        if compare == n:
            answer += 1
    return answer