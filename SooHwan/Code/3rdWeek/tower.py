def solution(heights):
    answer = []
    for i in range(0,len(heights)):
        answer.append(0)
        for j in range(i-1,-1,-1):
            if heights[i]<heights[j]:
                answer[i] = j+1
                break
    return answer