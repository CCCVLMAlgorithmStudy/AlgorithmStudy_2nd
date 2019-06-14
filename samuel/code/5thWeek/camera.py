def solution(routes):
    answer = 0
    routes.sort()
    camera = [0] * len(routes)
    preCam = 0
    for i in range(len(routes)-1,-1,-1):
        if camera[i] == 0 :
            preCam = routes[i][0]
            answer += 1
        for j in range(0,i) :
            if camera[j] == 0 and routes[j][1] >= preCam :
                camera[j] = 1
    return answer