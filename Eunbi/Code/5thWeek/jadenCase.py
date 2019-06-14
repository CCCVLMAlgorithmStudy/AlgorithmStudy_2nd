def solution(s):
    splitS = s.split(" ")
    num = 0
    for i in splitS:
        splitS[num] = i.capitalize()
        num+=1
    answer = ' '.join(splitS)
    return answer