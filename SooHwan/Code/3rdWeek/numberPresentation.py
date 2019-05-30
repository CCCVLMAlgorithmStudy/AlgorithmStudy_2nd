def solution(n):
    answer = 1
    doubleN = 2*n

    for a in range(n):
        for b in range(a+1,n):
            temp = (b+1)*b - (a+1)*a 
            if temp == doubleN:
                answer+=1
                break
            elif temp>doubleN:
                break
    return answer