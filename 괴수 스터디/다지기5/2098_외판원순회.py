
N = int(input())

INF = int(1e9)
dp = [[INF]*(1<<N) for _ in range(N)]

def dfs(x, visited):
    if visited == (1 << N) - 1:     
        if graph[x][0]:             
            return graph[x][0]
        else:                       
            return INF

    if dp[x][visited] != INF:       
        return dp[x][visited]

    for i in range(1, N):           
        if not graph[x][i]:         
            continue
        if visited & (1 << i):      
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
        
    return dp[x][visited]


graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))