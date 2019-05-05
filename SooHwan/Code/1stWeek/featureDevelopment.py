def solution(progresses, speeds):
    answer = []
    requireDays = []
    size = len(progresses)
    
    for i in range(0,size):
        requireDays.append(int(((99-progresses[i])/speeds[i])+1))

    i = 0
    while  i < size:
        count = 0
        reqDay = requireDays[i]
        while i != size and requireDays[i] <= reqDay:
            count+=1
            i+=1
        answer.append(count)
        
    return answer

progresses = [100,100,100]

speeds = [1,2,3]

print(solution(progresses,speeds))