def solution(n, lost, reserve):
    a = [1] * n
    for i in lost:
        a[i-1]=0
    for i in reserve:
        a[i-1]+=1
    for k,v in enumerate(a):
        if a[k] == 0:
            if a[k-1] > 1:
                a[k-1]=a[k]=1
            elif a[k+1] > 1:
                a[k+1]=a[k]=1
    a = list(filter(lambda x: x > 0, a))
    answer = len(a)
    # print(a)
    return answer