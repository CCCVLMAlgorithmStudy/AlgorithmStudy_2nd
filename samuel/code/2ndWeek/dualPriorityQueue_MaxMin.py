def solution(op):
    answer = []
    arr = []
    for i in op :
        if "I" in i :
            arr.append(int(i[2:]))
        else : 
            if not arr :
                continue
            Max = max(arr)
            Min = min(arr)
            if "D 1" in i :
                arr.remove(Max)
            else :
                arr.remove(Min)
    if not arr :
        answer.append(0)
        answer.append(0)
    else :
        answer.append(int(max(arr)))
        answer.append(int(min(arr)))
    return answer