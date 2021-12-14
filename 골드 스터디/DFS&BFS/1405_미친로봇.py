'''

n번의 행동을 츃마

4개의 방향 중 임의로 선택


로봇이 같은곳을 한번보다 많이 이동하지 않을 때 단순 들렸던 곳을 다시 들리지 않는경우

ex -제자리와도 같은곳 한번더
그러니까 들렸던곳 들리는경우도 단순 x

이동횟수는 총 14보다 작거나 같은 자연수, 
한쪽 방향으로만 가는 경우를 생각했을 때 30 x 30 사이즈의 2차원배열 생성

한 경우가 겹치않도록 깊이 이동  ==> dfs 방식으로 접근


'''
def dfs(x,y,percent,count):
    global result
    # 남 북 서 동
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    # print(result,percent,count)

    # 종료조건
    if count == C:
        # 한 경우가 겹치지 않고 이동한 경우
        result += percent
        return
    
    for i in range(4):
        # 범위를 나갈 일은 없다.
        # 확률 확인
        if i == 0:
            per = E/100
        elif i == 1:
            per = W/100
        elif i == 2:
            per = N/100
        else:
            per = S/100

        
        #이동 좌표 확인        
        cx = x + dx[i]
        cy = y + dy[i]
        if visit[cx][cy] == 0 and per != 0:
            visit[cx][cy] = 1
            dfs(cx,cy,percent*per,count+1)
            visit[cx][cy] = 0


# 입력
C, E, W, N, S = map(int,input().split())
# 확률
result = 0
# 최대 이동거리 배열 생성, 로봇을 정중앙 위치 14,14
visit = [[0]*30 for _ in range(30)]
visit[14][14] = 1
dfs(14,14,1,0)

print(result)
