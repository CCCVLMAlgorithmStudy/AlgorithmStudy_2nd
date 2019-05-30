def solution(n):
    return 0 if n==0 else 1 if n==1  else (solution(n-1)%1234567+solution(n-2)%1234567)%1234567