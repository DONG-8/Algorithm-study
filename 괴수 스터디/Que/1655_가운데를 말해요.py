# 중간의 작은 수를 구해야함
# 정렬을 통해 최소 값을 기준으로 정렬되게 하는 것은  heapq가 가장 빠름
# 그렇기 때문에 heapq를 사용하면 될 것으로 생각함.
# N 10만

import heapq
import sys

n = int(sys.stdin.readline())
left_heap = []
right_heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -1 * num)
    else:
        heapq.heappush(right_heap, num)
    
    if right_heap and left_heap and right_heap[0] < -1 * left_heap[0]:
        left_bigger_than_right_num = heapq.heappop(left_heap) * -1
        right_smaller_than_left_num = heapq.heappop(right_heap)
        heapq.heappush(left_heap,right_smaller_than_left_num * -1)
        heapq.heappush(right_heap, left_bigger_than_right_num)
    
    print(left_heap[0]*-1)
