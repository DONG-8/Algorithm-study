import heapq
n,m = map(int, input().split())
n_dia = []
bags = []
for i in range(n):
    a = list(map(int, input().split()))
    n_dia.append(a)

for i in range(m):
    bags.append(int(input()))

bags.sort()
n_dia.sort()
pq = []
j = 0 
answer = 0
for i in range(m):
    while j < n and n_dia[j][0] <= bags[i]:
        heapq.heappush(pq, -n_dia[j][1])
        j+= 1
    if pq: 
        answer += heapq.heappop(pq)

print(-answer)