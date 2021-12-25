'''
N-Queen 문제는 크기가 N x N 인 체스판 위에 퀸 N개를
서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을
작성하시오

'''
from collections import deque

# 한 자리 방문 했으면 다음 행 찾아가는 재귀문
# 종료조건은 N이 되었을 때
def recur(x):

    for i in range(N):
        if visit[x][i] == 0:
            pass    
            
N = int(input())
visit = [[0]*N for _ in range(N)]


num = 0

recur(0)
# # 퀸이 있는 자리의 행과 열 각 대각선 방문처리 하는 함수
# def queen_gs(x,y):
#     # 행 & 열    
#     for i in range(N):
#         visit[i][y] = 1
#         visit[x][i] = 1

#     # 대삭선 교차 체크
#     dx = [1, -1, -1, 1]
#     dy = [1, 1, -1, -1]
#     q = deque()
#     q.append([x,y])
#     while q:
#         i,j = q.popleft()
#         for c in range(4):
#             cx = i + dx[c]
#             cy = j + dy[c]
#             if 0<= cx < N and 0<= cy < N and visit[cx][cy] == 0:
#                 visit[cx][cy] = 1
#                 q.append([cx,cy])