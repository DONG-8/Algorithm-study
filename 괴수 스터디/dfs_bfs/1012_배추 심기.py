from collections import deque

def bfs(x,y):
    global visit

    d = [(0,1),(1,0),(-1,0),(1,0)]
    sx,sy = x,y
    q = deque([])
    q.append((sx,sy))
    visit[sx][sy] = 1

    while q: 
        xx,yy = q.popleft()
        for i in range(4):
            nx = xx + d[i][0]
            ny = yy + d[i][1]
            if 0 <= nx < M and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                visit[nx][ny] = 1
                q.append((nx,ny))

T = int(input())
for _ in range(T):
    N,M,K = map(int, input().split())
    check = []      # 0번 idx 가 행, 1번 idx가 열
    arr = [[0]*N for _ in range(M)]
    visit = [[0]*N for _ in range(M)]
    
    for i in range(K):
        y,x = map(int, input().split())
        arr[x][y] = 1
        
    count = 0
    for i in range(M):
        for j in range(N):
            if visit[i][j] == 0 and arr[i][j] == 1:
                bfs(i,j)
                count += 1
    
    print(count)


