from collections import deque
def solution(number, k):
    num_dq = deque(number)
    res = [num_dq.popleft()]
    while num_dq:
        v = num_dq.popleft()
        while res and res[-1] < v and k != 0:
            res.pop()
            k -= 1
        res.append(v)
        while (not num_dq) and (k != 0):
            res.pop()
            k -= 1
    return ''.join(res)