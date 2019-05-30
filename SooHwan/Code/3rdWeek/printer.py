def solution(priorities, location):
    answer = 0
    prevPrintLocation = -1
    while True:
        m = max(priorities)
        for i in range(prevPrintLocation+1,prevPrintLocation+1+len(priorities)):
            index = i%len(priorities)
            if priorities[index] == m:
                answer+=1
                if index ==location:
                     return answer
                priorities[index] = 0
                prevPrintLocation = index