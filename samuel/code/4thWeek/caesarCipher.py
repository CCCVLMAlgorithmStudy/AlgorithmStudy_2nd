def solution(s, n):
    s = list(map(ord,s))
    for i in range(len(s)) :
        if s[i] + n < 65 :
            s[i] = 32
        elif s[i] < 91 and s[i] + n > 90 or s[i] + n > 122 :
            s[i] += n - 26
        else :
            s[i] += n
    s = ''.join(list(map(chr,s)))
    return s