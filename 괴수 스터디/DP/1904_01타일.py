'''
끝이 00 인 경우 
끝이 1 인경우
dp[n] = dp[n-1] + dp[n-2]
'''
n = int(input())
dp = [0]*1000010
dp[1] = 1
dp[2] = 2
for i in range(3,1000010):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[n])

