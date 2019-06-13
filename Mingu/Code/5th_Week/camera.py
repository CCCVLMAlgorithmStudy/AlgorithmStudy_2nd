def isAinRouteB(a,b):
        return True if b[0] <= a and a <= b[1] else False
        
        
def sameRoutes(a,b):
    rtn = []
    if isAinRouteB(a[0],b) or isAinRouteB(a[1],b) or isAinRouteB(b[1],a) or isAinRouteB(b[1],a):
        rtn = a+b
        rtn.sort()
        rtn.pop(0)
        rtn.pop()
    return rtn

        
def solution(routes):
    routes.sort(key=lambda x:x[0])
    answer = [[-30000,30000]]
    # answer.append(routes.pop())
    while routes:
        tmpA = answer.pop()
        tmpR = routes.pop(0)
        
        sr = sameRoutes(tmpA,tmpR)
        if sr:
            answer.append(sr)
        else:
            answer.append(tmpA)
            answer.append(tmpR)
        # print(answer)
    return len(answer)