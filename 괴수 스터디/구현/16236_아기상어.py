# 아기상어



## 자신보다 큰 칸은 지나갈 수 없고, 작을경우 지나갈 수 있다.
## 크기가 같은경우 먹을수는없지만 지나갈 수 있다.
## 1초에 상하좌우 인접한 한칸씩이동


# 먹을 수 있는 물고기가 없다면 엄마상어 도움 요청
# 먹을 수 잇는 물고기가 1마리라면, 그 물고기를 먹으러 간다.

# 먹을 수 잇는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    # 거리는 아기상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 개수의 최솟값이다.
    # 거리가 가까운 물고기가 많다면, 가장위
    # 그런 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

    # 먹은 칸은 빈칸이 된다.


from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 아기상어의 위치 탐색

x,y = 0,0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            x,y = i,j
            break

# 아기상어 크기, 이동, 먹은 카운트
size = 2
move_count = 0
eat = 0
# 방문처리

# 가장 가까이에 있는 자신보다 작거나 같은 fish를 찾는다.

def bfs(x,y):
    visit = [[0]*N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x,y,0))
    visit[x][y] = 1
    # 같은 레벨 혹은 자신보다 작은 물고기 탐색,
    # bfs 로직 자체가 이미 최단거리에 최적화되어있음
    eat = []
    while q:
        fx,fy,dist = q.popleft()
        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]
            # 같은 사이즈라면 이동 거리만 증가하고 좌표를 추가 해 준다.
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                # 사이즈별로 구별
                visit[nx][ny] = 1
                # 사이즈보다 작거나, 같다면
                if arr[nx][ny] == 0 or arr[nx][ny] == size:
                    q.append((nx,ny,dist + 1))
                elif 0 < arr[nx][ny] < size:
                    q.append((nx,ny,dist + 1))
                    eat.append((dist+1, nx, ny))
    if len(eat) >= 1:
        # 거리가 가깝고 왼쪽 위부터 정렬
        eat.sort(key = lambda x : (x[0],x[1],x[2]))
        return eat[0]
    else:
        return (-1,-1,-1)

while True:
    eating_fish = bfs(x,y)
    if eating_fish == (-1,-1,-1):
        break
    else:
        eat += 1
        move_count += eating_fish[0]
        if eat == size:
            eat = 0
            size += 1
        x,y = eating_fish[1],eating_fish[2]
        arr[x][y] = 0

print(move_count)





