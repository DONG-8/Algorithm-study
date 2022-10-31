import heapq
# 다익스트라

N,M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for i in range(M):
    A,B,C = map(int, input().split())
    arr[A].append((C,B))
    arr[B].append((C,A))

# 경로 만들어주기

# 두 섬간의 좌표를 알아야함
s,e = map(int,input().split())

visit = [0]*(N+1)
q = []
heapq.heappush(q,(-9999999999999999999999,s))

for i in range(len(arr)):
    arr[i].sort(reverse=True)

# 각 노드까지의 최소값을 비교하고, 해당지점까지의 값은 최대값을 저장함
while q:
    # 큐가 무조건 작은값부터 꺼냄, 일부러 음수를 넣어서 큰값을 꺼내게 하고 다시 양수로 계산
    cost,now = heapq.heappop(q)
    # heapq를 위한 - 변환
    cost = -1*cost
    if now == e:
        break
    
    # 현재 방문한곳까지의 중량이 저장된 최대 중량보다 작다면
    # 이미 유효하지 않음
    if cost < visit[now]:
        continue
    
    for i in range(len(arr[now])):
        nc,nx = arr[now][i]
        # 다음 지점까지의 현재 경로에서의 최대중량
        next_cost = min(nc,cost)
        if next_cost > visit[nx]:
            visit[nx] = next_cost
            heapq.heappush(q, (-next_cost,nx))    
print(visit[e])