'''
음식물 피하기
'''
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1

    cnt = 1
    while q:
        x,y = q.popleft()

        for k in range(4):
            cx = x + dx[k]
            cy = y + dy[k]
            if 0 <= cx < N and 0 <= cy < M:
                if ls[cx][cy] == 1 and visit[cx][cy] == 0:
                    visit[cx][cy] = 1
                    cnt += 1
                    q.append([cx,cy])
    
    return cnt



N, M, K = map(int, input().split())

ls = [[0]*(M) for _ in range(N)]
visit = [[0]*(M) for _ in range(N)]
for i in range(K):
    r,c = map(int, input().split())
    ls[r-1][c-1] = 1


food_size = 0
for i in range(N):
    for j in range(M):
        if ls[i][j] == 1 and visit[i][j] == 0:
            food_size = max(food_size,bfs(i,j))
            
print(food_size)

