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
        answer = [0,0]
    else :
        answer = [max(arr),min(arr)]
    return answer