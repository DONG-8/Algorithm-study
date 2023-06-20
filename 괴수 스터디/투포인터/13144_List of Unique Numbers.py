n = int(input())
arr = list(map(int, input().split()))
s,e = 0,0
check = [0] * 100001    # 해당 숫자가 있는지 없는지 체크하기 위한 배열
count = 0
while e < n:
    if not check[arr[e]]:
        check[arr[e]] += 1
        e += 1
    else:
        count += (e-s)
        check[arr[s]] -= 1  # 동일한 숫자가 발견되었기 때문에, 스타트 포인트를 증가시킴
        s += 1
# 끝점에 도달하기 까지 s 지점의 경우의수는 구하지 못했음
# e 가 끝에 도달했다는것은 끝점의 숫자와 중복이 없다는것
count += (e-s)*(e-s+1) // 2
print(count)