def solution(n, money):
    dp = [0] * (n+2)
    for m in money:
        dp[m] += 1
        for i in range(1, n+1):
            if i - m > 0:
                dp[i] += dp[i-m]
    return dp[n]