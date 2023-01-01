def solution(board):
    dp = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    global_max = 0
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):

            if board[i-1][j-1] == 1:
                if board[i-2][j-1] == 1 and board[i-2][j-2] == 1 and board[i-1][j-2] == 1:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1
                if dp[i][j] > global_max :
                    global_max = dp[i][j]
    
    return global_max*global_max