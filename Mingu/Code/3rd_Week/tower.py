def solution(h):
    answer = []
    h.reverse()
    while h:
        tmp = h.pop(0)
        flag = len(h)
        for i in h:#reversed(h):
            if i > tmp:
                break
            flag-=1
        # answer.insert(0,flag)
        answer.append(flag)
    answer.reverse()
    return answer