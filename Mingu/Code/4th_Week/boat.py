def solution(people, limit):
    answer = 0
    people.sort()
    people.reverse()
    while people:
        tmp = people.pop(0)
        for i in people:
            if limit-tmp >= i:
                tmp += i
                people.remove(i)
                break
        answer+=1
    return answer