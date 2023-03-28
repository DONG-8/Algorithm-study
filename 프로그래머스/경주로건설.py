from collections import deque
def solution(board):
    answer = 9999999999999
    # 도로 총 길이
    n = len(board)
    # 방문 한 지점 확인하기
    dp = [[[10000] * n for i in range(n)] for j in range(4)]
    # 방향벡터
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([(0,0,0,0),(0,0,1,0),(0,0,2,0),(0,0,3,0)])
    while q:
        x,y,d,cost = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny <n and board[nx][ny] == 0:
                nc = cost + 1
                if i != d:
                    nc += 5
                if nc < dp[i][nx][ny]:
                    dp[i][nx][ny] = nc
                    if nx == n-1 and ny == n-1:
                        continue
                    q.append((nx,ny,i,nc))
                    
    
    for i in range(4):
        answer = min(answer,dp[i][n-1][n-1])

    return answer *100