def gcd(a,b):
    while b!=0:
        tmp = a%b
        a=b
        b=tmp
    return a

def lcm(a,b):
    return a * b // gcd(a,b)
    
def solution(arr):
    answer = 1
    while arr:
        answer = lcm(answer,arr.pop(0))
    return answer