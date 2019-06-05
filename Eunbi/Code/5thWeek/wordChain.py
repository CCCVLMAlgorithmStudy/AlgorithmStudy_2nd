def solution(n, words):
    
    p = 0 #몇번째 순서인지 체크
    player = 0 # 플레이어 체크
    turn = 0 # 몇 번째 턴인지 체크
    
    for i in words: # 첫번째 단어부터 리스트에 담긴 단어들을 모두 검사
        
        if player==0 or player==n: # 마지막 사람 차례가 끝나면 첫번째 사람으로오면서 턴 체크
            player = 1
            turn += 1
        else:
            player += 1
        
        if p > 0:
            if i[0] != last: # 첫 글자와 끝 글자가 같지 않으면
                answer = [player, turn] # 탈락한 사람의 번호와 턴을 리턴
                return answer
            if i in words[:p]: # 전에 나왔던 단어들 중에 같은 단어가 있으면
                answer = [player, turn] # 탈락한 사람의 번호와 턴을 리턴
                return answer
        p+=1
        last = i[-1]
    return [0, 0]