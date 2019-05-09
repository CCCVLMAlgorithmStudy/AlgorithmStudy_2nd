def solution(d, budget):
    answer = 0
    d.sort()    // sort : 정렬, 기본값은 오름차순 정렬, reverse옵션 True는 내림차순 정렬
    
    sum = 0
    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1
        else:
            break

    return answer
    
    
// 예산문제
// https://programmers.co.kr/learn/courses/30/lessons/12982
