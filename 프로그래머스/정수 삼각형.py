def solution(triangle):
    answer = 0
    # 기록 배열 만들기
    dp = []
    for i in range(1,len(triangle)+1):
        dp.append([0] * i)
    # 초기값 입력
    dp[0][0] = triangle[0][0]
    
    for i in range(len(triangle)):
        for j in range(i):
            dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])    
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]
    
    return max(dp[-1])