from collections import deque
def solution(order):
    answer = 1
    
    arr = deque(list(range(1,len(order)+1)))
    # 벨트 맨앞에 놓인 상자가 현재 트럭ㅇ ㅔ실어야하는 순서가 아니라면 다른곳 보관
    i = 0
    q = deque([])
    
    while i < len(order):
        if arr and arr[0] <= order[i]:
            a = arr.popleft()
            q.append(a)
        else:
            # 현재 숫자가 더 크다면?
            # 큐에서 찾아야겠지
            if q[-1] == order[i]:
                i += 1
                q.pop()
            else:
                break
            
    return i