def solution(n, lost, reserve):

    deserve = n - len(lost)
    
    for i in lost:
        
        front = i-1
        back = i+1
        
        if i in reserve:
            reserve.remove(i)
            deserve += 1
        elif front in reserve:
            reserve.remove(front)
            deserve += 1
        elif back in reserve:
            reserve.remove(back)
            deserve += 1
            
    return deserve