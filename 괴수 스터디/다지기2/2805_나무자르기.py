N, M = map(int,input().split())
tree = list(map(int, input().split()))

l = 0
r = max(tree)

max_height = 0
while l<=r:
    result = 0
    avg = (l+r)//2
    for i in tree:
        if i > avg:
            result += i-avg
    if result < M:
        r = avg - 1
    else:
        max_height = avg
        l = avg + 1
print(max_height)
