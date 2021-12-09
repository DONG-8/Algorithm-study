from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]

# 거리 거리 확인용
dist = [[-1] * m for _ in range(n)]  

q = deque()

# 시작점 체크
q.append((0,0))
dist[0][0] = 0

# 한무반복
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 다 -1 에서 바뀌게 될 예정
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

# 마지막 프린트
print(dist[n-1][m-1])