## bfs + simulation
# -1 : 검, 0 : 빨, 1~m : 빨강과 다른 어떤 색

# 폭탄 묶음이 없을때까지 반복
# 폭탄묶음 -> 2개이상의 연결된 같은색 또는, 빨강 + 같은색 2개
# 빨강만으로 이루어지면 묶음 x

# 반시계 90도 회전
# 다시 중력 drop
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
# 1. 폭탄 묶음 찾기 -> 원소별로 있어야 하는 값
# 행 기준점 찾기, 열 기준점 찾기 -> 폭탄묶음을 찾으면서 동시에 수행

# list형, [총 갯수, 빨강돌의 갯수, 행기준점, 열기준점, 시작지점의 좌표]
# 열 기준점의 경우 최솟값이므로 -1 을 곱해주어, 가장 큰 값을 기준으로 정렬 시켜준다.

# 경우 탐색
flag = True
temp = [
    [-4 for _ in range(n)]
    for _ in range(n)
]

def bfs(x,y):
    # 들어가야하는정보
    max_row,min_col = x,y
    count = 1
    red_count = 0
    visit = [[0]*n for _ in range(n)]
    # 탐색을 위한 초기 설정
    q = deque()
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visit[x][y] = 1
    color = arr[x][y]
    while q:
        a = q.popleft()
        sx,sy = a
        # 시작점의 색
        # 4방향 탐색
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] != -1:
                if arr[nx][ny] == color:
                    # 이 지점에서 기준점을 찾는 연산을 수행함
                    max_row = max(max_row, nx)
                    min_col = min(min_col,ny)
                    visit[nx][ny] = 1
                    count += 1
                    q.append((nx,ny))
                elif arr[nx][ny] == 0:
                    red_count += 1
                    count += 1
                    q.append((nx,ny))
                    visit[nx][ny] = 1
    # 빨강 1개 + 다른색 1개일경우
    if not count == red_count and count >= 2:
        bomb_list.append([count,-1 * red_count,max_row, -1 * min_col, x,y])

def bomb(x,y):
    q = deque()
    q.append((x,y))
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = 1
    color = arr[x][y]
    arr[x][y] = -4
    count = 1
    while q:
        sx,sy = q.popleft()
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] != -1 and arr[nx][ny] != -4:
                if color == arr[nx][ny] or arr[nx][ny] == 0:
                    arr[nx][ny] = -4
                    q.append((nx,ny))
                    visit[nx][ny] = 1
                    count += 1
    return count


# 중력 을통한 폭탄 아래로 내려주기
def drop():
    for i in range(n):
        for j in range(n):
            temp[i][j] = -4
    
    # Step2.
    for j in range(n):
        # 아래에서 위로 올라오면서
        # 해당 위치에 폭탄이 있는 경우에만 temp에 
        # 쌓아주는 식으로 코드를 작성할 수 있습니다.

        # 단, 돌이 있는 경우에는
        # 위에부터 쌓일 수 있도록 합니다.
        last_idx = n - 1
        for i in range(n - 1, -1, -1):
            if arr[i][j] == -4:
                continue
            if arr[i][j] == -1:
                last_idx = i
            temp[last_idx][j] = arr[i][j]
            last_idx -= 1
            
    # Step3. 다시 temp 배열을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

def rotate():
    for i in range(n):
        for j in range(n):
            temp[i][j] = -4

    # Step2.
    # 기존 격자를 반시계 방향으로 90도 회전했을 때의 결과를
    # temp에 저장해줍니다.
    for j in range(n - 1, -1, -1):
        for i in range(n):
            temp[n - 1 - j][i] = arr[i][j]

    # Step3.
    # 다시 temp 배열을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

while True:
    bomb_list = []
    # 하나의 폭탄 묶음을 찾았을 경우 방문처리를 통해 중복된 탐색 제거
    
    for i in range(n):
        for j in range(n):
            if (arr[i][j] == -1 or arr[i][j] == 0 or arr[i][j] == -4):
                continue
            bfs(i,j)

    if not bomb_list:
        break
    bomb_list.sort(reverse = True,key = lambda x : (x[0],x[1],x[2],x[3]))
    need_to_bomb = bomb_list.pop(0)
    a = bomb(need_to_bomb[-2],need_to_bomb[-1])
    answer += a*a
    drop()
    rotate()
    drop()

print(answer)