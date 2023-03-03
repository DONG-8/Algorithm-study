def solution(m, n, board):
    answer = 0
    boards = []
    for i in board:
        boards.append(list(i))
    # 4개의 접점이 되는 포인트 찾기
    # 다 동일한 것이라면 좌표 받기 -> list to set
    def find_four(x,y,Target):
        if Target == "X":
            return
        dx = [1,1,0]
        dy = [0,1,1]
        check_arr = []
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if boards[nx][ny] == Target:
                check_arr.append((nx,ny))
            else:
                return []
        return check_arr
    
    # 블록 빈칸 당겨주기
    def pull_block():       
        for j in range(n):
            for i in range(m):
                if boards[i][j] == "X":
                    for k in range(i,-1,-1):
                        boards[k][j] = boards[k-1][j]
                    boards[0][j] = "X"
    
    
    # 1. 모든 좌표에 대해서 제거 가능한 부분 찾기
    # 2. 제거 좌표변경 후 당겨주기
    # 3. 반복 -> 언제까지? -> 사라질 블록이 없을 때 까지
    while True:
        arr = []
        for i in range(m-1):
            for j in range(n-1):
                a = find_four(i,j,boards[i][j])
                if a:
                    a  += [(i,j)]
                    arr += a
        # 모든 좌표를 탐색했을 때 제거 할 블록이 없다면 중지
        if not arr:
            break
        # 아니라면 해당 블록의 값을제거 해 준다.
        else:
            arr = list(set(arr))
            answer += len(arr)
            for x,y in arr:
                boards[x][y] = "X"
            
            pull_block()
            
    return answer
    
    
    
    