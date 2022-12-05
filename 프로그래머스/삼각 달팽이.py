from collections import deque
def solution(n):
    answer = []
    # dfs 로 특정 경로로 향하게 한다.
    final_num = sum(list(range(1,n+1)))
    # 빈 배열 생성
    arr = [[0]*n for _ in range(n)]
    
    # 이제 이 배열에 특정 규칙대로 숫자를 넣어준다.
    # 그냥 처음은 아래로 -> 다음은 오른쪽 -> 왼대각
    dx = [1,0,-1]
    dy = [0,1,-1]
    # 초기 좌표 및 더해질 숫자, 방향을 나타내는 숫자
    x,y = 0,0
    num = 1
    dirt = 0
    arr[x][y] = num
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        
        if num == final_num:
            break
        
        nx = x + dx[dirt]
        ny = y + dy[dirt]
        
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            # 가는 방향에 대해서 방향을 초과 안하고 0이라는 값이 있다면
            num += 1
            arr[nx][ny] = num
            q.append((nx,ny))
        else:
            dirt = (dirt+1) % 3
            q.append((x,y))
            
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
    return answer