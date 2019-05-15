def solution(op):
    answer = []
    arr = []
    for i in op :
        if "I" in i :
            arr.append(int(i[2:]))
        elif "D" in i : 
            arr.sort()
            if not arr :
                continue
            elif "D 1" in i :
                arr.pop()
            else :
                arr.reverse()
                arr.pop()
    if not arr :
        answer.append(0)
        answer.append(0)
    else :
        answer.append(int(max(arr)))
        answer.append(int(min(arr)))
    return answer