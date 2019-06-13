def solution(n, words):
    answer = [0,0]
    before = []
    before.append(words[0][0])
    count = 0
    while words:
        count+=1
        people_num = 1
        for i in range(1,n+1):
            if words:
                tmp = words.pop(0)
                # print(before,tmp)
                if before[-1][-1]!=tmp[0] or tmp in before:
                    answer = [people_num,count]
                    words = []
                    # print(before,tmp)
                    break
                before.append(tmp)
                people_num+=1
        
    # # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer