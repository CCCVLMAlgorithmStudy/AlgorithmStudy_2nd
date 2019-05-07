def solution(prices):
    answer = []
    for i in range(0,len(prices)):
        time = 0
        for j in range(i+1,len(prices)):
            if j!= len(prices):
                time+=1
            if prices[i]>prices[j]:
                break
        answer.append(time)
    return answer