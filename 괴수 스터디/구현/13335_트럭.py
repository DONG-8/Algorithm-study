from collections import deque
n,w,l = map(int, input().split())
arr = list(map(int, input().split()))
q = deque([0]*w)
i = 0
count = 0
while i < n:
    q.popleft()
    b = sum(q) +(arr[0])
    if b > l:
        q.append(0)
    else:
        q.append(arr[0])
        arr.pop(0)
        i += 1    
    count += 1
print(count+w)