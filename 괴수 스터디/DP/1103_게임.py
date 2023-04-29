N,M = map(int, input().split())
arr = [list(input()) for _ in range(N)]


start = (1,1)
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 순환여부 체크 -> 방문처리의 목적이 들렸던 곳을 들리는지 체크 하기 위함임
visit = [[0] * (M+1) for _ in range(N+1)]
dp = [[0] * (M+1) for _ in range(N+1)]
def check(x,y):
    return (1<= x <= N and 1<=y<=M)

def bfs(x,y):
    # 범위 밖이거나 , 구멍을 만났다면 0을 돌려보내셈
    if  (not check(x,y)) or arr[x-1][y-1] == "H":
        return 0
    # 만약 들렸던 곳을 다시 들린다면?
    if (visit[x][y] != 0):
        print(-1)
        exit()
    # 이미 경로를 지나면서 갈 수 있는 경우에 대한 값이 있는 경우 메모 한 값을 return
    if dp[x][y]:
        return dp[x][y]
    # 위의 모든 종료 조건을 통과했다면, 지금 내 위치를 방문처리
    visit[x][y] = 1
    count = dp[x][y]
    for i in range(4):
        nx = x + dx[i] * int(arr[x-1][y-1])
        ny = y + dy[i] * int(arr[x-1][y-1])
        count = max(count, bfs(nx,ny) + 1)
    dp[x][y] = count    
    visit[x][y] = 0

    return count

a = bfs(1,1)
print(a)