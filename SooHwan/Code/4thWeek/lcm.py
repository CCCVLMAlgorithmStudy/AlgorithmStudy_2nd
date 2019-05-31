def gcd(a,b):
    if a==b:
        return a
    if a<b:
        temp = a
        a = b
        b = temp
    while b!=0:
        temp = a%b
        a = b
        b = temp
    return a
def gcm(a,b):
    return (a*b)//gcd(a,b)
def solution(arr):
    totalGCM = 1
    for i in arr:
        totalGCM = gcm(totalGCM,i)
    return totalGCM