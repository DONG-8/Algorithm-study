N, S = map(int, input().split())

arr = list(map(int, input().split()))

l,r = 0,0

# 초기 토탈 값 설정
total = arr[0]
small_length = int(1e9)
while l <= r and r < N:

    if total >= S:
        length = r - l + 1
        # 최소길이 갱신
        if length < small_length:
            small_length = length
        
        total -= arr[l]
        l += 1
        continue
    else:
        r += 1
    
    if r == N: break
    total += arr[r]

if small_length == int(1e9):
    print(0)
else:
    print(small_length)
