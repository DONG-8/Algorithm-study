# 최소 신장트리를 위한 uf
def solution(n, costs):
    answer = 0
    par = list(range(n))
    print(par)
    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]
        
    def union(x,y):
        x = find(x)
        y = find(y)
        
        if x > y:
            par[x] = y
        else:
            par[y] = x
        
    costs.sort(key = lambda x : x[2])
    for i in range(len(costs)):
        if find(costs[i][0]) != find(costs[i][1]):
            union(costs[i][0],costs[i][1])
            answer += costs[i][2]
    return answer

