import heapq
N = int(input())
q = [list(map(int, input().split())) for _ in range(N)]
q.sort()
arr = [q[0][1]]
q.pop(0)

for s,e in q:
    if arr[0] <= s:
        heapq.heappop(arr)
    heapq.heappush(arr,e)

print(len(arr))
    