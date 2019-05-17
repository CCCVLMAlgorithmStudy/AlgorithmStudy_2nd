def solution(n, lost, reserve):
    arr = [1] * n
    for i in lost :
        if not i in reserve :
            arr[i-1] = 0
        else :
            reserve.remove(i)
    for i in range(len(arr)-1) :
        if arr[i] == 0 :
            if i == 0 and 2 in reserve :
                arr[0] = 1
            elif ((i-1)+1) in reserve :
                arr[i] = 1
                reserve.remove((i-1)+1)
            elif((i+1)+1) in reserve :
                arr[i] = 1
                reserve.remove((i+1)+1)
    return sum(arr)