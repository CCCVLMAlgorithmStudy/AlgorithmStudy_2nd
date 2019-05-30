def solution(s,n):
    answer = ''
    for i in s:
        if i.isalpha():
            num = ord(i)
            if num < 91: #대문자
                num+=n
                if num > 90:
                    num-=26
            else: #소문자
                num+=n
                if num > 122:
                    num-=26
            tmp = chr(num)
        else:
            tmp = i
        answer += tmp
    return answer

# A 65 : Z 90
# a 97 : z 122