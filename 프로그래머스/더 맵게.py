import heapq
def solution(scoville, K):
    answer = 0
    # 힙으로 사용하기 전 정렬을 통해 꺼내오게 한다.
    scoville.sort()
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            c = a + b*2
            heapq.heappush(scoville, c)
            answer += 1
    
    if len(scoville) <= 1 and scoville[0] < K:
        return -1
    return answer