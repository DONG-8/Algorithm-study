from collections import deque

def bfs(x,y,arr,visit):
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    num = int(arr[x][y])
    visit[x][y] = 1
    q = deque()
    q.append((x,y))
    
    while q:
        sx,sy = q.popleft()
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and visit[nx][ny] == 0 and arr[nx][ny] != "X":
                visit[nx][ny] = 1
                q.append((nx,ny))
                num += int(arr[nx][ny])
                
    return num
    
    
    

def solution(maps):
    answer = []
    
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visit[i][j] == 0 and maps[i][j] != "X":
                answer.append(bfs(i,j,maps,visit))
    
    if answer == []:
        return [-1]
    answer.sort()
    return answer