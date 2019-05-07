def solution(number, k):
    answer = ''

    prevIter = -1
    thisIter = -1
    size = len(number)
    while k>0 and prevIter + k +1< size:
        max = '0'
        rangeLast = size if prevIter+2+k>size else prevIter+2+k
        for i in range(prevIter+1,rangeLast):
            if max<number[i]:
                max = number[i]
                thisIter = i
        if max == '0':
            thisIter += 1
        answer += max
        k -= (thisIter - prevIter -1)
        prevIter = thisIter
    if k==0:
        rest = number[prevIter+1:]
        answer+=rest
    return answer

number = '12345678'

k = 7

print(solution(number,k))