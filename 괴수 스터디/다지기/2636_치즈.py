from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def find_side_cheeze():
    # 매번 방문처리를 새롭게 해 주어야함
    visited =  [[0]*garo for _ in range(sero)]

    q = deque()
    # 초기 위치 설정
    q.append([0,0])
    visited[0][0] = 1
    # 겉의 치즈 수 세기
    count = 0

    # bfs 시작
    while q:
        x, y  = q.popleft()
        
        # 좌표탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내고 방문안했다면,
            if 0 <= nx < sero and 0 <= nx < garo and not visited[nx][ny]:
                if cheeze_list[]