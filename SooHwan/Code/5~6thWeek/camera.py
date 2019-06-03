def solution(routes):
    answer = len(routes)
    
    routes.sort(key = lambda x:x[0])
    prevInterval = routes[0]

    for interval in routes[1:]:
        if prevInterval[1]>=interval[0]:
            answer-=1
            if prevInterval[1]>interval[1]:
                prevInterval = [interval[0],interval[1]]
            else:
                prevInterval = [interval[0],prevInterval[1]]

        else:
            prevInterval = interval


    return answer