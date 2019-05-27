def lcm(a,b):
    gcm = 1
    for i in range(2,min(a,b)+1):
        while (a%i == 0) and (b%i ==0):
            a //= i
            b //= i
            gcm *= i
            continue
    lcm = gcm * a * b
    return lcm
def solution(arr):
    answer = 0
    for i in range(0,len(arr)-1):
        arr[i+1] = lcm(arr[i],arr[i+1])
    return arr[-1]