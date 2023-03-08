import heapq
N, M = map(int,input().split())
arr = list(map(int, input().split()))

# 오래 걸리는 케이스가 있으면 먼저 넣어준다.
concent = [0] * M
arr.sort(reverse= True)

heap = []
for con in arr:
    if len(heap) < M:
        heapq.heappush(heap,con)
    else:
        a = heapq.heappop(heap)
        heapq.heappush(heap, a + con)

print(max(heap))

# time = 0
# # 초기 값 설정
# for i in range(M):
#     a = arr.pop(0)
#     concent[i] = a

# while arr:
#     time += 1
#     for i in range(M):
#         if time - concent[i] >= 0:
#             a =  arr.pop(0)
#             concent[i] += a
#         if not arr:
#             break