def solution(priorities, location):   
    answer = 1
    Max = max(priorities)
    while priorities :
        if Max == priorities[0]:
            if location == 0:
                break
            priorities.remove(priorities[0])
            Max = max(priorities)
            location -= 1
            answer += 1
        else :
            if location == 0 :
                location += (len(priorities)-1)
            else :
                location -= 1
            priorities.append(priorities[0])
            priorities.remove(priorities[0])
    return answer