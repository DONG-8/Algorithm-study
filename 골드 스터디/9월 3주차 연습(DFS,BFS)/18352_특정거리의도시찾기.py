'''

단방향 도로임을 주의하자.

같은 도시는 거리 0
도시간 거리 1

도시의 갯수 n
도로의 갯수 m
우리가 구하려고하는 도시의 거리 k
출발하는 도시의 번호 x

출력은 거리가 k인 도시

인접 리스트 만들 때 양방향을 고려할 필요가 없다.

1. dfs --> 가는 경우의 수 최소값 입력
최소값이 구해지고 난 후 이 값을 K와 비교

2. BFS
최단거리 문제이기 때문에 BFS가 가장 구하기 최적화 되어 있다.
'''

import sys
sys.stdin = open('test.txt')


n, m, k, x = map(int, sys.stdin.readline().split())

vector = [[] for _ in range(n+1)]


# 인접 리스트 생성
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    vector[start].append(end)
# print(vector)
'''
# dfs 함수 지정
# x -> 시작지점
def dfs(x,dep):
    if dep == k:
        visit_local.append(x)
        return

    if dep < k:
        more_short.append(x)

    # 방문처리

    for j in vector[x]:
        if visited[j] == 0:
            visited[j] = 1
            dfs(j,dep+1)
            visited[j] = 0

# 단방향이라도 서로 연결된 경우도 있을 것이다.
# 그렇다면 결국 방문 처리를 해 주어야하고,
visited = [0]*(n+1)
# 방문지역 저장을 위한 빈 리스트 생성
visit_local = []
more_short = []

# 자기 자신에게 도착하게 되었을 때는 0으로 처리해 주어야한다.
if k == 0:
    print(x)
else:
    visited[x] =1
    # 0 이 아닐때
    dfs(x,0)
    # print(visit_local)
    # print(more_short)
    # print(vector)
    for i in more_short:
        if i in visit_local:
            visit_local.remove(i)

    # print(visit_local)

    if visit_local:
        for i in range(len(visit_local)):
            print(visit_local[i])
    else:
        print(-1)
'''

# print(vector)

# 시작지점
visited = [0]*(n+1)

# 큐 생성
que = []

# 시작지 정보 입력
que.append(x)

# 시작지점 방문처리
visited[x] = 1
count = 0
while que:
    if count == k:
        # 최소거리인 도시 출력
        break
    size = len(que)

    for i in range(size):
        a = que.pop(0)
        adj = vector[a]

        for j in adj:
            if visited[j]:
                continue
            visited[j] = 1
            que.append(j)




    count += 1

if que:
    que.sort()
    for i in range(len(que)):
        print(que[i])

elif k==0:
    print(x)
else:
    print(-1)








