# 최소 금액을 구하고, M번은 뽑아서 사용할 수 있는 금액을 찾는다

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))


def check(mid):
    now = mid
    count = 1
    for i in range(N):
        if now - arr[i] >= 0:
            now -= arr[i]
        else:
            count += 1
            now = mid
            now -= arr[i]
    if count <= M:
        return True
    else:
        return False

lo, hi = max(arr),1e9
min_num = hi
while lo <= hi:
    mid = (lo + hi) // 2

    if check(mid):
        hi = mid - 1
        mid_num = mid
    else:
        lo = mid + 1

print(int(mid_num))
