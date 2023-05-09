import sys
sys.setrecursionlimit(1000004)

dp = [float('inf')] * 1000004
INF = 987654321

# trace
def go(here):
    if here == 0:
        return
    print(here, end=' ')
    if here % 3 == 0 and dp[here] == dp[here // 3] + 1:
        go(here // 3)
    elif here % 2 == 0 and dp[here] == dp[here // 2] + 1:
        go(here // 2)
    elif here - 1 >= 0 and dp[here] == dp[here - 1] + 1:
        go(here - 1)

n = int(input())
dp[1] = 0
# 최소 경로 누적하여 찾아내기
for i in range(1, n + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[n])
go(n)