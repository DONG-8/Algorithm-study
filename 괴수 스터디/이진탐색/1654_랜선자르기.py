# 1 <= K <= 10000, 1 <= N <= 1,000,000
# 그리디 or 이분탐색

# 최대 길이를 구한다  -> 이분탐색을 통해 일치하는 값의 범위를 좁혀 나간다.

## 데이터 입력
# 최대 길이에서 1부터 최대길이까지 값을 구하고, 그 값에 나눠지는지 확인
# 값이 나오면 오른쪽, 나오지 않으면 왼쪽 탐색
# 끝가지 확인한 마지막 값이 답

K,N = map(int, input().split())
line = [int(input()) for _ in range(K)]
l,r = 1, max(line)
while l <= r:
    mid = (l+r)//2
    count = 0
    for i in range(K):
        count += line[i]//mid

    if count < N:
        r = mid - 1
    else:
        l = mid + 1
print(r)

# 