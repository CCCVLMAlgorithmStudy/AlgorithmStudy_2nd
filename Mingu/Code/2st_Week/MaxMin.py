def solution(s):
    tmp = list(map(lambda x:int(x),s.split(' ')))
    
    return str(min(tmp))+" "+str(max(tmp))