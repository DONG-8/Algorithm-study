n = int(input())
arr = list(map(int, input().split()))
number = int(input())
count = 0
arr.sort()  # 정렬을 통해 양 끝에서 맞는 쌍을 찾게함
l,e = 0, n-1

while l < e:
    if arr[l] + arr[e] > number:
        e -= 1
    elif arr[l] + arr[e] < number:
        l += 1
    else:
        # 같은 경우 왼쪽의 수를 늘려준다.
        l += 1
        count += 1

print(count)