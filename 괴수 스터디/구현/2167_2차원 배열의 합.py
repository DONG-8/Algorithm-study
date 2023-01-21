N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
# 2차원 누적합 구하기
dp = [[0]*(M+1) for _ in range(N+1)]
# 해당 지역까지의 모든 누적합 구하기
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for k in range(K): # 10000
    i,j,x,y = map(int, input().split())
    # 300 * 300 90000
    # 시간 오바지
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])