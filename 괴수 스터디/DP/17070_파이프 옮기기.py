n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0] for k in range(n+1)] for _ in range(n+1)]

# 초기 값 설정
dp[1][2][0] = 1

for i in range(2,n+1):
    if arr[0][i-1] == 1:
        break
    dp[1][i][0] = 1

# 점화식 기반 작성
for i in range(2,n+1):
    for j in range(1,n+1):
        if arr[i-1][j-1] == 0 and arr[i-1][j-2] == 0 and arr[i-2][j-1] == 0:
            dp[i][j][1] = sum(dp[i-1][j-1])
        if arr[i-1][j-1] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[n][n]))

