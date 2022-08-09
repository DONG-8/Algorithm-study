N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]

# 끝까지 구간합 구하기 
# 2차원 dp

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

# 해당 구간에서 부분 집합을 구해야함

max_num = -1000000000
# 각 x,y 좌표 그리고 그 좌표로부터 갈수있는 모든 구간까지만의 합
# 영역의 시작점을 x,y 끝점을 i,j로 잡는다고하면

for i in range(1,N+1):
    for j in range(1,M+1):
        for x in range(i,N+1):
            for y in range(j,M+1):
                max_num = max(max_num, dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])


print(max_num)