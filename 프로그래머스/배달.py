import heapq

def solution(N, road, K):
    answer = 0
    # 최단거리 갱신
    arr = [[] for _ in range(N+1)]
    for i in range(len(road)):
        a,b,c = road[i]
        arr[a].append((c,b))
        arr[b].append((c,a))
    dp = [1e9 for _ in range(N+1)]
    heap = []
    dp[1] = 0
    heapq.heappush(heap,(0,1))
    
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in arr[node]:
            nc = c + cost
            if nc < dp[n]:
                dp[n] = nc
                heapq.heappush(heap,(nc,n))
        
    for i in range(1,len(dp)):
        if dp[i] <= K:
            answer +=1
    return answer