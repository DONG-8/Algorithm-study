from collections import deque
F,S,G,U,D  = map(int, input().split())

arr = list(range(F+1))
visit = [-1]*(F+1)
q = deque()
q.append(S)
visit[S] = 0
dx = [U,-D]
flag = False
while q:
    now = q.popleft()
    for i in range(2):
        nx = now + dx[i]
        if 1 <= nx <= F and visit[nx] == -1:
            visit[nx] = visit[now] + 1
            q.append(nx)

            if nx == G:
                flag = True
    if flag == True:
        break

if visit[G] == -1:
    print('use the stairs')
else:
    print(visit[G])
