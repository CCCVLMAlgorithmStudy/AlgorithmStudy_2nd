def solution(p, l):
    answer = 0
    while p:
            tmp = p[0]
            print("!"+str(l))
            l-=1
            if tmp >= max(p):
                p.pop(0)
                answer+=1
                print(p)
                if l == -1:
                    
                    break;
            else:
                p.append(p.pop(0))
                if l < 0:
                    l = len(p)-1
    return answer