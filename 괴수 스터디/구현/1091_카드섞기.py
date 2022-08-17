from copy import deepcopy
N = int(input())    # 3의 배수
P = list(map(int, input().split()))
S = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append(i % 3)
# 처음 상태로 돌아왔을 때 종료
# 처음상태 기록
first = arr[:]
count = 0
# 초기랑 같지 않을 때 종료
while True:
    if arr == first and count != 0:
        print(-1)
        break
    
    if arr == P:
        print(count)
        break
    
    change =[0]*N
    for i in range(N):
        change[i] = arr[S[i]]

    arr = change
    count += 1