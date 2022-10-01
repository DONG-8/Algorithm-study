'''
# 양방향 연결 완료, 이게 집인지 맥인지, 스벅인지 구문해야함
# 집 0, 맥1, 스벅2
# 각 점에서의 최단거리를 알아야함, 각 집의 code를 돌아야함

# 1. 하나의 집에서 시작
# 최단거리를 구한다 라는 행위는 변하지 않음

# 한 지점마다의 최단 거리 기록이 나올거임, dp로 치면 각 정점까지의 최단거리가 나올것
# 이때, 각 node의 번호를 알고 있으니 여기서 탐색해서 빼내면 끝 아님?

# 근데이걸 각 집별 노드에 적용시켜야함

# 맥도날드나, 스벅에 도착했다고 끊으면 안됨  why? 맥이랑 스벅 연결되면 우짤껴?
# 그렇기 때문에 각 지점의 최종 값을 확인 해야함, 조건부 확인을 위한건 여기 있음
# 한 지점에 대해서 탐색하고, mac_ndoe
#
'''
import heapq

def daik(n):
    # 메모
    dp = [9999999999999 for _ in range(V+3)]
    # 빈 큐 생성
    q = []
    
    # 스벅의 노드값 or 맥도날드의 노드 값이 들어옴 [2,3,4,5,]
    heapq.heappush(q, [0,n])
    dp[n] = 0
    
    while q:
        cost,idx = heapq.heappop(q)
        
        # 가지치기
        # 이지점까지 오는데 쓰인 비용이 저장된 비용보다 크다면 돌아가
        if dp[idx] < cost:
            continue

        
        for nx_cost,nx_idx in node[idx]:
            if nx_idx == V + 1 or nx_idx == V + 2:
                # 가상노드를 거쳐서 또 다른곳으로 가버리면 답없쥬?
                continue
            
            if nx_cost + cost < dp[nx_idx]:
                dp[nx_idx] = nx_cost + cost
                heapq.heappush(q, [nx_cost+cost, nx_idx])
    return dp
    
    # mac_min = 9999999999999999999999999999999999
    # star_min = 9999999999999999999999999999999999
    
    # for k in mac_node:
    #     if mac_min > dp[k] and dp[k] <= mac_dist:
    #         mac_min = dp[k]
    
    # for j in star_node:
    #     if star_min > dp[j] and dp[j] <= starbux_dist:
    #         star_min = dp[j]
            
    # if mac_min == 9999999999999999999999999999999999 or star_min ==9999999999999999999999999999999999:
    #     return 9999999999999999999999999
    # else:
    #     return mac_min + star_min

V,E = map(int, input().split())

# 각 idx 번호를 통해 연결된 node를 체크한다.
node = [[] for _ in range(V+3)]
for i in range(E):
    x,y,c = map(int, input().split())
    node[x].append([c,y])
    node[y].append([c,x])

mac,mac_dist = map(int, input().split())
mac_node = list(map(int,input().split()))
starbux, starbux_dist = map(int, input().split())
star_node = list(map(int, input().split()))
# 맥 만족, 스벅만족 따로임 어떻게 하나 똑같음
result = 9999999999999999999999999

# 시간 초과가 나는 이유는 모든 집마다 각 노드의 거리를 구해야함, 근데 문제에서  준 정점의 갯수는 1만
# 그럼 이걸 다 돌리면 당연히 시간 초과가 남

# 그럼 각 집에서 가장 가까운 맥도날드와 스벅이 한번에 구해져야함

# 다익스트라의 원리를 보면,
# 하나의 지점에서의 연결된 노드를 탐색함
# 한번에 여러지점에서 시작을 시켜야 이 부분이 해결됨
# 시작점, 원래 시작점 (cost, start)를 기준으로 연결 된 노드들을 탐색하면서 최단거리를 찾음

# 여러지점을 시작점으로 두는 방법 --> **가상 노드 --> 이걸 어케아냐고;;

for i in mac_node:
    # 스타벅스의 지점
    node[V+1].append([0,i])
    node[i].append([0,V+1])

for i in star_node:
    # 스타벅스의 지점
    node[V+2].append([0,i])
    node[i].append([0,V+2])

a = daik(V+1)
b = daik(V+2)

result = 9999999999999999999999999999999999999999

for i in range(1,V+1):
    if i in mac_node:
        continue
    if i in star_node:
        continue

    if a[i] <= mac_dist and b[i] <= starbux_dist:
        result = min(result, a[i] + b[i])
if result == 9999999999999999999999999999999999999999:
    print(-1)
else:
    print(result)




# 이렇게 하면 node의 시작점을 V+1로 만들었을 때 모든 스타벅스 지점을 시작기준으로 각 집마다의 맥과의 최단거리를 구할 수 있다.

# for i in range(1,V+1):
#     # 정점의 갯수만큼 순회할거임!
#     # 근데 이게 맥도날드나, 스벅이면? 알 필요가없지?
#     # 가지치기 드가자
#     if i in star_node or i in mac_node:
#         continue
#     else:
#         # print(i, "집이에요")
#         # 여기서 다익트스라 순회
#         a = daik(i)
#         result = min(result,a)

# if result ==9999999999999999999999999:
#     print(-1)
# else:
#     print(result)