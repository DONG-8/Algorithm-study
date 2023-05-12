N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()
# 가까운 녀석,

end_time = -1

for start,end in arr:
    if end_time > start:
        start += end_time - start
    else:
        end_time = start
    end_time += end

print(end_time)