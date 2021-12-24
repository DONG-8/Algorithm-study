N,K,B = map(int, input().split())

arr = [1]*(N+1)
# 변경해주기
for i in range(B):
    a = int(input())
    arr[a] = 0

# print(arr) [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]

# 연속된 K개의 신호등이 존재하도록
# K개의 연속된 구간의 합이 K 이면 된다

guganhap = sum(arr[:K])
max_num = 0
# 10 - 5 + 1 --> 6
for i in range(N-K+1):
    guganhap = guganhap - arr[i] + arr[K+i]
    if guganhap > max_num:
        max_num = guganhap

print(K-max_num)