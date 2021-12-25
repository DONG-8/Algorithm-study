'''
야민정음

치환이 가능한 몇개의 문자들이 정해져 있다.

'''
import heapq

# A -> B 로 바뀌기
A, B = map(int,input().split())

N, M = map(int, input().split())

# N + 1 개의 노드 만들기
node = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

INF = int(1e9)
distance = [INF for i in range(N+1)]
q = []
heapq.heappush(q, [0,A])
distance[A] = 0

while q:
    c, idx = heapq.heappop(q)

    if c > distance[idx]:
        continue

    for i in node[idx]:
        if c + 1 < distance[i]:
            distance[i] = c + 1
            heapq.heappush(q, [c+1,i])

if distance[B] == INF:
    print(-1)
else:
    print(distance[B])