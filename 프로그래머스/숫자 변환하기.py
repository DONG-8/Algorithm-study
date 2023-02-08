def solution(x, y, n):
    answer = 0
    # 1차원 방문배열을 이용한 최단거리 측정 bfs 이용
    visit = [0] * (y+1)
    arr = [2,3,n]
    q = [x]
    cnt = 0
    if x == y:
        return 0
    while q:
        a = q.pop(0)

        for i in range(3):
            if i == 2:
                na = a + n
            else:
                na = a * arr[i]

            if na <= y and visit[na] == 0:
                visit[na] = visit[a] + 1
                q.append(na)
                if na == y:
                    return visit[na]
    return -1