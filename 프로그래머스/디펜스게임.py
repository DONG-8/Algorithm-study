import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    heapq.heapify(heap)
    # logn 이 되는 경우 파라매트릭 서치(이분탐색)
    # 힙큐  -> logn
    # 힙을 어케쓰노
    for i in range(len(enemy)):
        heapq.heappush(heap,enemy[i])
        
        if len(heap) > k:
            answer += heapq.heappop(heap)
            
        
        if answer > n:
            return i


    return len(enemy)
