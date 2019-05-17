def find(unionFind,u):
    if u==unionFind[u]:
        return u
    else:
        p = find(unionFind,unionFind[u])
        unionFind[u] = p
        return p
def union(unionfind,x,y):
    x = find(unionfind,x)
    y = find(unionfind,y)
    unionfind[y] = x
def solution(n, costs):
    answer = 0
    link = 0
    unionFind = [i for i in range(n)]
    costs.sort(key = lambda cost:cost[2])
    for cost in costs:
        if find(unionFind,cost[0])!= find(unionFind,cost[1]):
            answer+=cost[2]
            union(unionFind,cost[0],cost[1])
            link += 1
        if link == n-1:
            break
    return answer