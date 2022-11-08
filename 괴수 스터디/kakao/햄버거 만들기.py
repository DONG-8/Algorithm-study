from collections import deque

def solution(ingredient):
    cnt = 0
    q = deque(ingredient)
    # 하나씩 빼서 확인
    check = deque()
    while q:
        a = q.popleft()
        check.append(a)
        if a == 1 and len(check) >= 4:
            x = []
            for i in range(-1,-5,-1):
                x.append(check[i])
            if x == [1,3,2,1]:
                cnt += 1
                for i in range(4):
                    check.pop()
    return cnt

