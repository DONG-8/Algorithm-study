N,M = map(int, input().split())
arr = list(map(int, input().split()))

# n 값은 블루레이의 길이
# M 등분이 되는지 체크하고 많으면 길이를 늘리고
# 체크된 갯수가 작거나 같으면 길이를 줄이고

def check(mid):
    global arr
    blue_lay = []
    number = 0
    for i in range(N):
        number += arr[i]
        if number > mid:
            number -= arr[i]
            blue_lay.append(number)
            number = arr[i]
    if number != 0:
        blue_lay.append(number)
    return blue_lay

l,r  = 0, sum(arr)
answer = 0
while l <= r:
    mid = (l + r) //2
    new = check(mid)
    if len(new) <= M:
        answer = max(new)
        r = mid -1
    else:
        l = mid + 1

print(answer)