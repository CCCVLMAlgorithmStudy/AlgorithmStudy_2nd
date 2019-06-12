def solution(s):
    
    a = s.lower()
    L = a.split(" ")
    
    
    print(L)
    answer = ""
    for i in L :
        i = i.capitalize()
        answer = answer + i + " "

    return answer[:-1]

//https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

