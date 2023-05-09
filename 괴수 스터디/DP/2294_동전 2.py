N,K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

# 입력을 받고, dp에 저장
dp = [1000001] * (1000001)
# dp에 시작하는 값을 알아야함
arr.sort(reverse=True)
for i in range(len(arr)):
    dp[arr[i]] = 1

for i in range(1,K+1):
    for j in range(N):
        if i - arr[j] >= 0:
            dp[i] = min(dp[i-arr[j]] + 1, dp[i])

if dp[K] >= 1000001:
    print(-1)
else:
    print(dp[K])