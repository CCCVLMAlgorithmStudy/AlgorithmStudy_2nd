def solution(operations):
    answer = []
    for o in operations:
        type,num = o.split(' ')
        if type=="I":
            answer.append(int(num))
        else:
            if len(answer) > 0:
                answer.pop(answer.index( max(answer) if num=="1" else min(answer) ))
    return [0,0] if len(answer) == 0 else [max(answer),min(answer)]