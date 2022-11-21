from collections import deque
def solution(prices):
    answer = []
    arr = deque(prices)
    while arr:
        a = arr.popleft()
        count = 0
        for i in arr:
            count += 1 
            if i < a:
                break
    
        answer.append(count)
    return answer