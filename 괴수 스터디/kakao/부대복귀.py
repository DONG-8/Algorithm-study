def solution(n, roads, sources, destination):
    answer = []
    arr = [[] for _ in range(n+1)]
    # 반대로 가자
    
    # 우선 연결
    for i in range(len(roads)):
        a,b = roads[i]
        arr[a].append(b)
        arr[b].append(a)
    
    # 시작지점을 1을 기반으로 1과 연결된곳만 찾고, 나머지 -1처리
    visit = [-1]*(n+1)
    visit[destination] = 0
    q = []
    q.append(destination)
    while q:
        now = q.pop(0)
        for k in range(len(arr[now])):
            nx = arr[now][k]
            if visit[nx] == -1:
                visit[nx] = visit[now] + 1
                q.append(nx)
    
    for j in  sources:
        answer.append(visit[j])

    return answer