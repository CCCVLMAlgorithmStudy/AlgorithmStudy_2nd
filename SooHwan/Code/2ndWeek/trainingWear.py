def solution(n, lost, reserve):
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
             
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    return n -len(lost)