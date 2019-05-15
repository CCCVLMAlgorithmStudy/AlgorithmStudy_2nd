def solution(op):
    answer = []
    arr = []
    for i in op :
        if "I" in i :
            arr.append(int(i[2:]))
        elif "D" in i : 
            if not arr :
                continue
            arr.sort()
            if "D 1" in i :
                arr.pop()
            else :
                arr.reverse()
                arr.pop()
    if not arr :
        answer = [0,0]
    else :
        answer = [max(arr),min(arr)]
    return answer