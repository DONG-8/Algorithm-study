import heapq

def solution(operations):
    answer = []
    
    while operations:
        o, num = operations.pop(0).split()
        if o == "I":
            heapq.heappush(answer,int(num))
        elif answer and o == "D" and int(num) > 0:
            answer.pop()
        elif answer and o == "D" and int(num) < 0:
            answer.pop(0)
    if answer == []:
        return [0,0]
    return [max(answer), min(answer)]