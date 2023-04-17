N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 정보를 저장시킬 dp 생성
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    weight = arr[i][0]
    value = arr[i][1]
    for j in range(1,M+1):
        # j는 무게
        if j < weight:
            # 이전 까지의 최대 무게
            dp[i+1][j] = dp[i][j]
        else:
            # 만약 같거나 크다면 현재 내 물건을 가방에 넣고, 나머지칸에 이전 최선의 값을 넣어준다
            dp[i+1][j] = max(value + dp[i][j-weight],dp[i][j])

print(dp[-1][-1])