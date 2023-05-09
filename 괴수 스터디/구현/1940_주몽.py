N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
# 갑옷은 두개의 재료로 만든다,
# 그럼 양끝 수에서 작으면 왼쪽 포인터 이동
l , r = 0, len(arr)-1
while l < r:
    total = arr[l] + arr[r]
    if total < M:
        l += 1
    elif total > M:
        r -= 1
    else:
        answer += 1
        l += 1

print(answer)