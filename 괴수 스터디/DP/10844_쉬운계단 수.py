n = int(input())

# dp = [9]
# for i in range(1,n):
#     dp.append(dp[i-1]*2 - (i))

# print(dp[n-1])

# 끝자리가 만들어질 수 있는 경우를 찾기
# .    0 1 2 3 4 5 6 7 8 9
# 1자리 0 1 1 1 1 1 1 1 1 1
# 2자리 1 1 2 2 2 2 2 2 2 1
# 3자리
# .
# 
# 행 100 열 10 
arr = [[0]*10 for _ in range(101)]

# 한자리수는 0을 제외한 모든 값이 1 이다
for i in range(1,10):
    arr[0][i] = 1

for i in range(1,101):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][1]
        elif j == 9:
            arr[i][j] = arr[i-1][8]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

print(sum(arr[n-1]))


