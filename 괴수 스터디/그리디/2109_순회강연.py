# day안에 가면 됨. 그럼
# 1 333 이면 3이 2번 사용도 가능한거지,
# 내가 가게 된 일수를 체크해서 내부적으로 있는지도 체크해야함
import heapq
N = int(input())
arr = []

for i in range(N):
    n,d = map(int, input().split())
    arr.append((d,n))
arr.sort(key = lambda x : (x[0],-x[1]))
stack = []

for i in range(N):
    day, pay = arr.pop(0)
    heapq.heappush(stack,pay)
    if len(stack) > day:
        heapq.heappop(stack)

print(sum(stack))