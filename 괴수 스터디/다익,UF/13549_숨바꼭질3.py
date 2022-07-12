from collections import deque


N, K = map(int, input().split())

# 걷거나 순간이동을 할 수 있다.

# 수빈이가n, 동생 k

visit = [0]*100001
que = deque()
que.append(N)

while que:
    loc = que.popleft()
    if loc == K:
        print(visit[loc])
        exit()
    dx = [loc+1 , loc-1, loc*2]
    for i in dx:
        # 위치가 범위 내에 있고 방문하지 않은 장소라면
        if 0 <= i < 100001 and visit[i] == 0:
            # 순간이동은 visit 그대로 가기
            if i == loc*2 and 1 != 0:
                visit[i] = visit[loc]
                que.appendleft(i)
            # 그 외에 한칸 앞뒤 이동
            else:
                visit[i]  = visit[loc] + 1
                que.append(i)
