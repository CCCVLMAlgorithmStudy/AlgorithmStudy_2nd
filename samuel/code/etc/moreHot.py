import asyncio
def solution(scoville, K):
    Q = asyncio.PriorityQueue()
    answer = 0
    for i in scoville :
        Q.put_nowait(i)
    v = Q.get_nowait()
    while v < K :
        if Q.qsize() < 1:
            answer = -1
            break
        Q.put_nowait(v + Q.get_nowait() * 2)
        answer += 1
        if Q :
            v = Q.get_nowait()
    return answer