T,W = map(int, input().split())

# 자리가 바뀐 횟수! 바뀐거 vs 안바뀐거
# 누적합 만으로는 완성할 수 없음
plum = []
for i in range(T):
    plum.append(int(input()))

# 결국 1이 더해지는지 안더해지는지의 차이, 단 차이가 있다면 w에 따라 달라짐
dp = [[0] * (T+1)  for _ in range(W+1)]
for i in range(T):
    if plum[i] == 1:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1] 

if plum[0] == 2:
    dp[1][0] =1

arr = [[0] * (T+1) for _ in range(W+1)]

for i in range(W+1):
    for j in range(T):
        if i % 2 == 0:
            if plum[j] == 1:
                arr[i][j] = 1
        else:
            if plum[j] == 2:
                arr[i][j] = 1
# print(arr)
for i in range(1,W+1):
    for j in range(1,T):
        dp[i][j] = max(dp[i-1][j-1] + arr[i][j], dp[i][j-1] + arr[i][j])
# print(dp)
answer =0
for i in range(W+1):
    answer = max(answer, dp[i][-2])

print(answer)
            