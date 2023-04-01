import heapq
def solution(jobs):
    answer = 0
    n = len(jobs)
    start,end = 0,0
    heap = []
    heapq.heapify(jobs)
    while jobs or heap:
        while jobs:
            k = heapq.heappop(jobs)
            if start <= k[0] <= end:
                heapq.heappush(heap,[k[1],k[0]])
            else:
                heapq.heappush(jobs,k)
                break
        
        if heap:
            time, point = heapq.heappop(heap)
            start = end
            end += time
            answer += (end - point)
        else:
            end += 1
    
    return answer//n