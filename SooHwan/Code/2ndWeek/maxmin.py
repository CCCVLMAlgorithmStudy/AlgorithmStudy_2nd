def solution(s):
    l = list(map(int,s.split(" ")))
    answer = [min(l),max(l)]
    return " ".join(map(str,answer))