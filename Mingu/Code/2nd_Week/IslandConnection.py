def solution(n, costs):
    check = [0]*n
    costs = sorted(costs, key=lambda cost: cost[2])
    first = costs.pop(0)
    check[first[0]]=check[first[1]]=1
    answer = first[2]
    
    for c in costs:
        if abs(check[c[0]]-check[c[1]])==1:
            check[c[0]]=check[c[1]]=1
            answer += c[2]
        if sum(check)==n:
            break;
    return answer