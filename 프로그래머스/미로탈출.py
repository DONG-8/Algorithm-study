def bfs(s,e,maps,start_count):
    sx,sy = s
    # 모든 순회가 끝났을 때 해당 지점의 visit point
    visit = [[-1]*len(maps[0]) for _ in range(len(maps))]
    visit[sx][sy] = start_count
    q = [(sx,sy)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]    
    while q:
        x,y = q.pop(0)    # 0번째 값을 뺀다
        if x == e[0] and y  == e[1]:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and  0 <= ny < len(maps[0]) and visit[nx][ny] == -1 and maps[nx][ny] != "X":
                q.append((nx,ny))
                visit[nx][ny] =visit[x][y] + 1
        
    return visit[e[0]][e[1]]

def solution(maps):
    answer = 0
    h = len(maps)
    w = len(maps[0])
    visit =[ [0] * w for _ in range(h)]
    # 2번 이동하면 됨
    # 2단계가 있지 -> 1. 라벨에도 못가는경우 , 2. 라벨에는 갔지만 출구로 못가는 경우
    # s -> L , L -> E
    for i in range(h):
        for j in range(w):
            if maps[i][j] == "S":
                s = [i,j]
            elif maps[i][j] == "L":
                l = [i,j]
            elif maps[i][j] ==  "E":
                e = [i,j]
    
    la= bfs(s,l,maps,0)
    if la == -1:
        return -1
    else:
        ea = bfs(l,e,maps,la)
        return ea
