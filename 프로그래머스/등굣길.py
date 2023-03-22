def solution(m, n, puddles):
    visit = [[0] * (m+1) for _ in range(n+1)]
    for i,j in puddles:
        visit[j][i] = 1
    visit[0][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if visit[i][j]:
                visit[i][j] = 0
            else:
                visit[i][j] = (visit[i-1][j] + visit[i][j-1])% 1_000_000_007

    return visit[-1][-1] 