# 결국 그래프 최소비용 탐색
# 간선의 가중치가 존재하므로 다익스트라
import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start_point = int(sys.stdin.readline())

# 각 간선의 가중치 정보 확인을 위한 리스트


node_weight = [[] for _ in range(V+1)]

# 최소 가중치 비교를 위한, 미리 inf 에 가까운 or 상당히 큰 숫자를 이용한 리스트 생성
# 앞으로 비교를 위해서 사용 될 예정임
INF = int(1e9)
distance = [INF for i in range(V+1)]

# print(node_weight)
for i in range(E):
    s, e, cost = map(int,sys.stdin.readline().split())
    node_weight[s].append([cost, e])

que = []
# 시작노선, 가중치 0 초기화
heapq.heappush(que, [0, start_point] )

# 가중치 비교 위치 0 으로 초기화

distance[start_point] = 0

while que:

    dis, idx = heapq.heappop(que)

    if distance[idx] < dis:
        continue

    # 각 인덱스 번호를 가져왔다.

    # 현재 위치에서 갈 수 있는 위치들을 한번 보자

    # 현재까지 쌓아 온 가중치 + 현재에서 다음으로 가는 가중치 vs 시작~ 다음 위치까는 가중치보다 작다면 업데이트
    # 어떻게?

    for i in node_weight[idx]:
        node_hap = distance[idx] + i[0]     # 현 지점까지의 거리 + 다음 가는 인덱스의 가중치
        # i[0] 다음으로 가는 노드 정보
        if distance[i[1]] > node_hap:
            distance[i[1]] = node_hap
            heapq.heappush(que, [node_hap, i[1]])


for i in range(len(distance)):
    if i == 0:
        continue

    if distance[i] == int(1e9):
        print('INF')
        continue

    print(distance[i])



