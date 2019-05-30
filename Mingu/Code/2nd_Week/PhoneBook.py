def solution(phone_book):
    answer = True
    pb = sorted(phone_book)
    # pb = sorted(phone_book,key=lambda x:(x,len(x)))
    for i in range(0,len(pb)-1):
        v = pb[i]
        if v == pb[i+1][0:len(v)]:
            answer = False
    return answer