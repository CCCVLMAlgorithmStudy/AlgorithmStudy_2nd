def solution(s, n):
    answer = ''
    Lowercharacters = 'abcdefghijklmnopqrstuvwxyz'
    Uppercharacters = Lowercharacters.upper()
    for c in s:
        if c in Lowercharacters:
            answer+= Lowercharacters[(Lowercharacters.index(c)+n)%26]
        elif c in Uppercharacters:
             answer+= Uppercharacters[(Uppercharacters.index(c)+n)%26]
        else:
            answer+=c
    return answer


print(solution("a B z	",4))