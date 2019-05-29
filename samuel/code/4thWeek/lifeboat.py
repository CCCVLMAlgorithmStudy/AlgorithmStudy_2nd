def solution(people, limit):
    answer, i = 0, 0
    people.sort()
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit :
            i += 1
        j -= 1
        answer += 1
    return answer