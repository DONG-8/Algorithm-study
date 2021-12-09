import sys
sys.stdin = open('test.txt')

N, M = map(int, input().split())

tetromino = [list(map(int,input().split())) for _ in range(N)]
ls = []
# 현재 칸 기준 3칸 가면 ㅗ 제외 모든 도형
def dfs(x,y,cnt,suma):
    if cnt == 3:
        # print(suma)
        ls.append(suma)
        return

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if  0 <= cx < N and 0 <= cy < M and visited[cx][cy] == 0:
            visited[cx][cy] = 1
            dfs(cx,cy,cnt+1,suma+tetromino[cx][cy])
            visited[cx][cy] = 0

fuu = []
def ppaque(x,y,cnt,plus):
    # 빠큐모양 돌리기

    if cnt == 3:
        ls.append(plus)
        # print(x,y,plus)
        return

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # 본인 기준 상하좌우 탐색

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < N and 0 <= cy < M and fuck_u_visit[cx][cy] == 0:
            fuck_u_visit[cx][cy] = 1
            ppaque(x,y,cnt+1,plus + tetromino[cx][cy])
            fuck_u_visit[cx][cy] = 0



fuck_u_visit = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        visited[x][y] = 1
        fuck_u_visit[x][y] = 1
        dfs(x,y,0,tetromino[x][y])
        ppaque(x, y, 0, tetromino[x][y])
        visited[x][y] = 0
        fuck_u_visit[x][y] = 0

print(max(ls))