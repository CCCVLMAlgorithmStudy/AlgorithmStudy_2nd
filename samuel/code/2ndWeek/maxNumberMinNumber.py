def solution(s):
    answer = [int(i) for i in s.split(' ')]
    return str(min(answer)) + " " + str(max(answer))
# 아래 코드를 짧게 표현한 것이 위의 코드
#    answer = []
#    s = s.split(' ')
#    for i in s :
#        answer.append(int(i))
#    return str(min(answer)) + " " + str(max(answer))