# 입력단계
N = int(input())
arr = list(map(int, input().split()))

# 정렬
arr.sort()

# 투포인터로 각 포인트별 최소 값을 찾아낸다.

# 시작점 끝점 설정
start = 0
end = N-1

# 초과하지 않을때까지 탐색

# 최소값 비교를 위한 큰 수 지정
# sum_of_fluide = int(1e9)
sum_of_fluide = 10000000000000000000
# 찾아야하는 result -> 두용액의 합이 최소인경우, 이때 시작점 끝점을 print

x,y = 0,0
while start < end:

    # 시작점 끝점 합 현재 최소값과 비교
    if sum_of_fluide > abs(arr[start] + arr[end]):
        sum_of_fluide = abs(arr[start] + arr[end])
        x,y = arr[start], arr[end]

    # 이동
    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1
    
print(x,y)