'''
# 테두리가 맞냐 아니냐로 좀 구분이 되어야함
    # 바깥 테두리의 영역인 i,j로 1 내부 2로 변경
    
    # 다음 겹치고 테두리만 어떻게 구분할거냐?
    # -->2인곳에 1(테두리) 를 할려고 하면 pass
    # -->1인곳에 2을 그릴려고 하면 2를 덮어씌움 어짜피 영역임 그렇게 하면
    # 될 줄 알았더니 2번 case에서 반례가 생김
    
    # --> 1칸 차이임 그럼 다 돌고나서 내부 빈 공간 즉 양끝 테두리임을 감지하고, 이를 칠해줘야함 --> 1이 연속으로 나오면 변인데 이걸 어케하누?
    
    # 변 1짜리가 문제임 1 바로 옆에 1이 있기때문에
    # 그럼 이 변 1짜리를 없게 변 길이를 모두 늘리고 나중에 경로값 /2 를 해줌
'''

def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque

    answer = 0
    # 2배로 늘리기 때문에
    
    arr = [[0]*102 for _ in range(102)]
    for rect in rectangle:
        sx,sy,ex,ey = map(int,rect)
        # 2배로 늘려주기
        ex,ey = ex*2, ey*2
        sx,sy = sx*2, sy*2
        for i in range(sx,ex+1):
            for j in range(sy,ey+1):
                
                if (i == sx or i == ex or j == sy or j == ey):
                    if arr[i][j] == 2:
                        continue
                    else:
                        arr[i][j] = 1
                else:
                    arr[i][j] = 2
    
    # print(arr)
        # 배치완료 bfs 탐색
    q = deque()
    q.append([characterX*2,characterY*2])
    visit = [[0]*102 for _ in range(102) ]
    visit[characterX*2][characterY*2] = 1
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    count = 0
    
    while q:
        x,y = q.popleft()
        
        if x == itemX*2 and y == itemY * 2:
            # print(x,y,'도착해쩌염')
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 101 and 0 <= ny < 101 and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append([nx,ny])
                visit[nx][ny] = visit[x][y] + 1

    
    return visit[itemX*2][itemY*2]//2