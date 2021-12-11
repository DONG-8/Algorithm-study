from collections import deque

N, M = map(int, input().split())

# 2번, 각 횟수별로 체크하는 방식을 넣자.

dx = [1,2,3,4,5,6]

q = deque()
ls = list(range(101))
# print(ls)
q.append(1)

for i in range(N+M):
    start, end = map(int, input().split())
    ls[start] = end

visit = [-1]*101
visit[1] = 0
while q:
    x = q.popleft()
    for k in range(6):
        cx = x + dx[k]
        if 0 < cx <= 100:
            cx = ls[cx]
            # print(cx,'cx')
            if visit[cx] == -1:
                visit[cx] = visit[x] + 1
                q.append(cx)

print(visit[-1])


'''
원 풀이
from collections import deque

N, M = map(int, input().split())

# 2번, 각 횟수별로 체크하는 방식을 넣자.

dx = [1,2,3,4,5,6]

q = deque()
ls = [0]*101
q.append(1)

for i in range(N+M):
    start, end = map(int, input().split())
    ls[start] = end

visit = [-1]*101
visit[1] = 0

while q:
    x = q.popleft()
    for k in range(6):
        cx = x + dx[k]
        if 0 < cx <= 100 and ls[cx] != 0 and visit[ls[cx]] == -1:
            # visit[cx] = visit[x] + 1
            visit[ls[cx]] = visit[x] + 1
            q.append(ls[cx])
        elif 0< cx <=100 and ls[cx] == 0 and visit[cx] == -1:
            visit[cx] = visit[x] + 1
            q.append(cx)


print(visit[100])

'''