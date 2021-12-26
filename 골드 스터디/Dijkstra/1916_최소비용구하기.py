'''
N개의 도시가 있다.
한도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
A번째 도시에서 B번째 도시까지 가는데 드는 비용을 최소화하려고한다.

최소비용 그래프 --> 다익스트라

'''
import heapq
import sys

def ds(S):
    q = []
    heapq.heappush(q,[0,S])
    cost[S] = 0

    while q:
        c, e = heapq.heappop(q)

        # 가지치기 현재 dp에 저장된 cost보다 더해줘야하는 c값이 크면
        # 이미 최소 비용이 아니기 때문에 가지치기
        if c > cost[e]:
            continue

        for goto in arr[e]:
            new_cost = c + goto[0]
            if new_cost < cost[goto[1]]:
                cost[goto[1]] = new_cost
                heapq.heappush(q,[new_cost,goto[1]])


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

arr = [[] for _ in range(N + 1)]
# print(arr)
for _ in range(M):
    s, e, c= map(int, sys.stdin.readline().split())
    arr[s].append([c,e])

S,E = map(int, sys.stdin.readline().split())
INF = int(1e9)
cost = [INF]*(N+1)

ds(S)
print(cost[E])


