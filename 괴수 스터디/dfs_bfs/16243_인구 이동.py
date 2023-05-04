from collections import deque
import math
N, L,R = map(int,input().split())
arr = [list(map(int, input().split())) for  _ in range(N)]

# 이걸로 그룹 체크
visit = [[-1] * N for _ in range(N)]
group_position = [] # 그룹이 시작되는 시작점 찾기


def bfs(x,y,idx):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    check = 1   # 그룹이 될 수 있는 갯수
    q.append((x,y))
    number = arr[x][y]
    visit[x][y] = idx
    while q:
        sx,sy = q.popleft()
        now_people = arr[sx][sy]
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0<= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and visit[nx][ny] != 999 and L <= abs(arr[nx][ny] - now_people) <= R:
                check += 1
                number += arr[nx][ny]
                visit[nx][ny]= idx
                q.append((nx,ny))

    if check == 1:
        return False
    else:
        new_number = math.floor(number / check)
        new_que = deque()
        new_que.append((x,y))
        new_visit = [[-1]*N for _ in range(N)]
        new_visit[x][y] = 0
        arr[x][y] = new_number
        while new_que:
            sx,sy = new_que.popleft()
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if 0<= nx < N and 0 <= ny < N and visit[nx][ny] == idx and new_visit[nx][ny] == -1:
                    arr[nx][ny] = new_number
                    new_visit[nx][ny] = 0
                    new_que.append((nx,ny))
        return True
# 경계선의 값 다 합치기 그리고 바꿔주기, -> 동시에할 수 있긴함
# count , total_people -> 해당 좌표들에 모든 값을 바꿔주기 1,2,3,4,5

def shake_people(number,check,idx,x,y):
    new_number = math.floor(number / check)
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((x,y))
    new_visit = [[-1]*N for _ in range(N)]
    new_visit[x][y] = 0
    arr[x][y] = new_number
    while q:
        sx,sy = q.popleft()
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0<= nx < N and 0 <= ny < N and visit[nx][ny] == idx and new_visit[nx][ny] == -1:
                arr[nx][ny] = new_number
                new_visit[nx][ny] = 0
                q.append((nx,ny))



def check_group(): # 인구이동 로직 적용
    count = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] != -1:
                continue
            if bfs(i,j,count):
                count += 1
            else:
                visit[i][j] = 999
    return count

answer = 0
while True:
    a = check_group() # 그룹의 수
    if a:
        visit = [[-1] * N for _ in range(N)]
        answer += 1
    else:
        break

print(answer)