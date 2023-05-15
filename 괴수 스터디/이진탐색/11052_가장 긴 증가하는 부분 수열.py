n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 1004
ret = 0

for i in range(n):
    mx = 0
    for j in range(i):
        if a[j] < a[i] and mx < cnt[j]:
            mx = cnt[j]
    cnt[i] = mx + 1
    ret = max(ret, cnt[i])

print(ret)