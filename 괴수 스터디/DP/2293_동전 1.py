N,K = map(int,input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

dp = [0] * (K+3)
dp[0] = 1

for c in coin:
    for i in range(c,K+1):
        if i-c < 0:
            continue
        dp[i] += dp[i - c]

print(dp[K])