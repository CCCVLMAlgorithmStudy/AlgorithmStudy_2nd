def solution(n, words):
    answer = [0, 0]
    check = []
    for i in range(len(words)-1) :
        check.append(words[i])
        if words[i][-1] != words[i+1][0] or words[i+1] in check:
            answer = [((i+1)%n)+1, (i+1)//n+1]
            break
    return answer