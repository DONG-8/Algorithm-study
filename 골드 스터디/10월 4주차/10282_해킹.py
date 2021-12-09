import heapq

T = int(input())

for t in range(T):

    node, edge, start_computer = map(int,input().split())

    # 연결 정보를 나타낼 리스트 작성
    node_list = [[] for _ in range(node+1)]
    for i in range(edge):
        s, e, cost = map(int,input().split())

        node_list[e].append([cost,s])

    que = []
    heapq.heappush(que, [0, start_computer])

    # 간선 가중치 확인을 위한 리스트
    INF = int(1e9)
    cost_find = [INF for _ in range(node+1)]

    cost_find[start_computer] = 0
    # print(node_list)
    # print(cost_find, node_list, que)
    # 큐가 존재할때까지 무한반복
    while que:

        # 큐에서 하나 추출 가장 가까운 거리
        cost, end_point = heapq.heappop(que)

        # 현 지점을 거쳐서 원하는 곳 까지가는 코스트가 스타트지점에서 직통으로 가는값이 더 작으면 갈 필요가없음
        if cost > cost_find[end_point]:
            continue

        for idx in node_list[end_point]:
            change_cost = cost_find[end_point] + idx[0]
            if change_cost < cost_find[idx[1]]:
                cost_find[idx[1]] = change_cost
                heapq.heappush(que, [change_cost,idx[1]])
    time = 0
    computer_count = 0
    for i in cost_find:
        if i == INF:
            continue
        
        computer_count +=1

        if i > time:
            time = i
    
    print(computer_count, time)
        


