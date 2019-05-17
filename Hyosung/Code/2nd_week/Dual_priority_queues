def solution(operations):
    import heapq
    answer = []
    priority_queue = []
    
    for operation in operations:
        op, num = operation.split()
        #insert
        if op == "I":
            heapq.heappush(priority_queue, int(num))
        #delete 
        elif op == "D" and priority_queue:
            #max data delete
            if num == "1":
                data = max(priority_queue)
                priority_queue.pop(priority_queue.index(data))
            #min data delete
            elif num == "-1":
                heapq.heappop(priority_queue)
    if priority_queue:
        #max
        answer.append(max(priority_queue))
        #min
        answer.append(heapq.heappop(priority_queue))
    else:
        answer = [0,0]
    return answer
