'''
N-Queen 문제는 크기가 N x N 인 체스판 위에 퀸 N개를
서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을
작성하시오

'''
# from collections import deque

# 각 행과 각 열에는 하나씩만 들어가야하며, 대각선 조건을 확인해야한다.
# 방문한 정보에 대해서 2차원으로 나타낼 필요가 없어진다.
def recur(x):
    global count

    # 종료조건
    if x == N:
        # 마지막행까지 들어갔다면, 카운트 증가
        count += 1
        return

    for i in range(N):
        # 인덱스 == 행, 내부 VALUE == 열을 의미
        # 대각선을 만족하는 행만 재귀에 들어감
        visit[x] = i
        if cross(x):
            recur(x+1)
        visit[x] = -1



# 퀸 공격범위 확인
def cross(x):
    # flag = True
    for i in range(x):
        # 대각선내에 있다면 같은 열이라면
        if visit[i] == visit[x] or x-i == abs(visit[i]-visit[x]):
            return False
    return True   


N = int(input())
visit = [-1]*N
sero = [False]*N
count = 0

recur(0)
print(count)



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