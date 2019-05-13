def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) <len(phone_book[i+1]):
            for j, c in enumerate(phone_book[i]):
                if c != phone_book[i+1][j]:
                    break
                if j == len(phone_book[i])-1:
                    return False
        else:
            for j,c in enumerate(phone_book[i+1]):
                if c != phone_book[i][j]:
                    break
                if j == len(phone_book[i+1])-1:
                     return False
    return answer