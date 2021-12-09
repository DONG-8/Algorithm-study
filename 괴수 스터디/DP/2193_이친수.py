'''
끝자리의 앞자리가 1인 경우에는 10이 되어야 하고
그 외에는 0 과 1 두가지 다 올 수 있다.

'''

n = int(input())

dp = [0]*(91)

dp[1] = 1
dp[2] = 1
for i in range(3,91):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

