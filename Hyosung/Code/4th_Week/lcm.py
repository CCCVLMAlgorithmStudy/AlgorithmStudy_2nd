def solution(num):

    answer = num[0]

    for i in range(1,len(num)):

        number = num[i]

        high = max(number,answer)

        low = min(number,answer)

        answer = high*low //gcd(high,low)

    return answer

def gcd(high,low):

    if low == 0 : return high

    else : return gcd(low,high%low)


