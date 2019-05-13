def solution(operations):
    pQ = []
    isSorted = True
    for command in operations:
        comm,num = command.split()
        
        if comm == 'I':
            pQ.append(int(num))
            isSorted = False
        elif comm == 'D':
            if len(pQ) == 0:
                continue
            else:
                if isSorted == False:
                    pQ.sort()
                    isSorted = True
                if num == '1':
                    pQ.remove(pQ[-1])
                elif num == '-1':
                    pQ.remove(pQ[0])
    if len(pQ) == 0:
        answer = [0,0]
    else:
        if isSorted == False:
            pQ.sort()
        answer = [pQ[-1],pQ[0]]
    return answer