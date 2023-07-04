def solution(board, skill):
    answer = 0
    # 행에 들어갈 숫자 0,0 -> 3,4
    # list로 정리가 되면 됨, # 시작점,시작점 해당 연산  -> 끝점, 시작점, 시작점, 끝점
    
    check = [[0] * (len(board[0])+2) for _ in range(len(board)+2)]
    for ty, r1,c1,r2,c2, degree in skill:
        tag = 1
        if ty == 1: # 공격
            tag *= -1
        check[r1][c1] += tag*degree
        check[r2+1][c1] += tag*degree*-1
        check[r1][c2+1] += tag*degree*-1
        check[r2+1][c2+1] += tag*degree
    
    for j in range(len(check[0])):
        for i in range(1,len(check)):
            check[i][j] += check[i-1][j]
    
    for i in range(len(check)):
        for j in range(1,len(check[0])):
            check[i][j] += check[i][j-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + check[i][j] > 0:
                answer += 1
    
    return answer