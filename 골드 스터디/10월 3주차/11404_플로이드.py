import heapq

# 결국 그래프 최소비용 탐색
# 정점의 수 1번부터 존재하기 때문에 생성시 n+1
n = int(input())


# 버스의 갯수 --> 각 정점을 잇는 노드와 가중치
m = int(input())

# 비용 최대치 미리 설정

busstation = [[] for _ in range(n+1)]
for i in range(m):
    s , e , cost = map(int, input().split())

    busstation[s].append([cost, e])
    # 양방향이 아니기 때문에 이대로 진행
    

for i in range(1,n+1):

    inf = int(1e9)
    distance = [inf for _ in range(n+1)]
    # 스타트 지정 및 스타트지점 가중치 0 설정
    distance[i] = 0
    que = []
    heapq.heappush(que, [0, i])

    while que:

        wt, idx = heapq.heappop(que)

        # 가지치기 이후에 구간의 코스트를 더하는 과정에서 distance[idx]보다 한 노드의 가중치가 더 크면 더했을때
        # 작은 경우가 나올 수 없기 때문이다.
        if distance[idx] < wt:
            continue
        
        # 현 위치에서 갈 수 잇는 노드들을 탐색
        for k in busstation[idx]:
            node_hap = distance[idx] + k[0] # 현재까지의 노드 가중치 + 앞으로 갈 방향의 가중치
            if node_hap < distance[k[1]]:
                distance[k[1]] = node_hap
                heapq.heappush(que, [ node_hap, k[1]])

    
    for i in range(len(distance)):
        if distance[i] == int(1e9):
            distance[i] = 0
    print(*distance[1:])
    








