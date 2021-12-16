'''
방향성 없는 그래프
최단거리 이동(다익스트라) + 임의로 주어진 두 정점은 반드시 통과 해야 한다 -->  v1을 기준으로

기존 다익스트라에 조건이 1개 더 추가된 경우이다.

문제의 조건
-- 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
-- 하지만 반드시 최단 경로로 이동해야 한다
'''
import heapq

def ds(start):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 배열을 반환
    return distance


# 입력받기
INF = int(1e9)
v, e = map(int, input().split())

# 방향배열을 위한 비어있는 리스트
graph = [[] for _ in range(v + 1)]
# 방향성 없는 그래프 두방향 추가
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

v1, v2 = map(int, input().split())
# 다익스트라

# 1, v1, v2 가 시작점일때 각 지점까지의 최단거리
original = ds(1)
v1_path = ds(v1)
v2_path = ds(v2)

# 1 -> v1 -> v2  -> N 경로
v1_result = original[v1] + v1_path[v2] + v2_path[v]
# 1 -> v2 -> v1  -> N 경로
v2_result = original[v2] + v2_path[v1] + v1_path[v]

# 둘중 최소 확인
result = min(v1_result, v2_result)

if result < INF:
    print(result)
else:
    print(-1)
