def fibo(fibos, n):
    if n==0 or n==1:
        return n
    else:
        if fibos[n]!=-1:
            return fibos[n]
        else:
            current = 2
            while current<=n:
                if fibos[current]==-1:
                    fibos[current]= (fibos[current-1]+fibos[current-2])%1234567
                current+=1
            return fibos[n]
    
def solution(n):
    fibos = [-1 for _ in range(0,n+1)]
    fibos[0] = 0
    fibos[1] = 1
    
    return fibo(fibos,n)