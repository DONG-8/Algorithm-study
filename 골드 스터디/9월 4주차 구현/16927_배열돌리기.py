import sys
sys.stdin = open('test.txt')

N, M, R = map(int, sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 방문처리를 위한 비어있는 리스트


# N,M이 둘다 홀수라면, 안움직여야하는 칸이 존재한다.
# 이를 미리 방문처리 하기에는 귀찮으니
# 배열을 돌리다가 정지해야할 좌표를 만나면 종료
# if N%2 == 1 and M%2 ==1:
#     if N >= M:
#         break_point = M//2
#         print(break_point)
#     else:
#         break_point = N//2
#         print(break_point)
# else:
#     break_point = 999

# 숫자만큼 이동시키겠다!
# print(arr[break_point][break_point])

def turn(x, y, arr, R):
    global start_x, start_y

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    if R == 0:
        k = 0
        while True:
            cx = x + dx[k]
            cy = y + dy[k]
            if 0<= cx < N and 0 <= cy < M and visited[cx][cy] == 0:
                visited[cx][cy] = -1
                if cx == start_x and cy == start_y:
                    break
                x, y = cx, cy

            else:
                k = (k + 1)%4


    count = 0
    for r in range(R):
        k = 0
        while True:
            cx = x + dx[k]
            cy = y + dy[k]
            if 0<= cx < N and 0 <= cy < M and ( visited[cx][cy] == 1 or visited[cx][cy] == 0) and visited[cx][cy] != -1:
                visited[cx][cy] = 1
                change_arr[cx][cy] = arr[x][y]
                if cx == start_x and cy == start_y:
                    count += 1
                    if count == R-1:
                        visited[cx][cy] = -1

                    else:
                        visited[cx][cy] = 1

                x, y = cx, cy

            else:
                k = (k + 1)%4


        for x in range(N):
            for y in range(M):
                arr[x][y] = change_arr[x][y]

        x = start_x
        y = start_y
# def fix_arr(i,j):
#     for x in range(i,N):
#         for y in range(j, M):
#             if visited[x][y] == 0 :
#                 que.append(arr[x][y])
#     # print(que)
#     a = que.pop()
#     ma = [a] + que
#     # print(ma)
#     for n in range(N):
#         for m in range(M):
#             if visited[n][m] == 0:
#                 visited[n][m] = 1
#                 change_arr[n][m] = ma.pop(0)


# que = []
# for i in range(N):
#     for j in range(M):
#         if visited[i][j] == 0:
#             print(arr)
#             R = R % ((N-1-i)*2 + (M-1-j)*2)
#             if R == 0:
#
#                 continue
#
#             for r in range(R):
#                 start_x, start_y = i, j
#                 turn(i,j,arr)

def turn_total(i,j,R,cnt):
    global start_y,start_x

    X = R % ((N - cnt) * 2 + (M - cnt) * 2)
    print(X)
    if visited[i][j] == 0:
        turn(i, j, arr, X)



change_arr = [[0] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        change_arr[x][y] = arr[x][y]


visited = [[0] * M for _ in range(N)]

i = 0
j = 0
cnt = 1
while True:
    start_x, start_y = i, j
    if visited[i][j] != 0:
        break
    turn_total(i,j,R,cnt)
    cnt += 2
    i += 1
    j += 1


for i in range(N):
    print(*change_arr[i])


