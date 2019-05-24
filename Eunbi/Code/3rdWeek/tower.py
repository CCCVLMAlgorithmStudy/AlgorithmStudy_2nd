def solution(heights):
    answer = []
    compare = []
    for i, v in enumerate(heights):
        compare.append(v)
        answer.insert(i, 0)
        for ii, vv in enumerate(compare):
            if v<vv:
                answer.insert(i, ii+1)
                del answer[i+1]
    return answer