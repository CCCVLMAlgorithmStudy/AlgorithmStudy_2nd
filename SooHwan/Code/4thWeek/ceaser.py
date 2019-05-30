def solution(s, n):
    answer = ''
    Lowercharacters = 'abcdefghijklmnopqrstuvwxyz'
    Uppercharacters = Lowercharacters.upper()
    
    table = str.maketrans(Lowercharacters+Uppercharacters,Lowercharacters[n:]+Lowercharacters[:n]+Uppercharacters[n:]+Uppercharacters[:n])
    answer = s.translate(table)
    return answer


print(solution("a B z	",4))