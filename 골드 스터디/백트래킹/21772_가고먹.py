'''
. 빈칸
# 장애물
G 가희
S 고구마


'''
# cnt는 깊이
def max_goguma(x,y,cnt,num):
    global eat_goguma
    
    # 종료조건
    if cnt == T:
        eat_goguma = max(eat_goguma,num)
        return

    # 해야 할 작업
    # 현 위치에서 좌표 변경
    for n in range(4):
        cx = x + dx[n]
        cy = y + dy[n]
        # 만약 범위내이고  & 장애물 아니라면 이동!
        if 0 <= cx < R and 0 <= cy < C and arr[cx][cy] != "#":
            # 방문처리 
            visit[cx][cy] = 1
            # 고구마라면 num 증가
            if arr[cx][cy] == "S":
                arr[cx][cy] = "."
                max_goguma(cx,cy,cnt+1,num+1)
                arr[cx][cy] = "S"
            else:
                max_goguma(cx,cy,cnt+1,num)
            visit[cx][cy] = 0



R, C, T = map(int,input().split())
visit = [[0]*C for _ in range(R)]
arr = [ list(input()) for _ in range(R)]
# 감사합니다....

# 방향벡터
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 시작지점 찾기
for i in range(R):
    for j in range(C):
        if arr[i][j] == "G":
            x = i
            y = j
            break
eat_goguma = 0
arr[x][y] = "."
max_goguma(x,y,0,0)

print(eat_goguma)
