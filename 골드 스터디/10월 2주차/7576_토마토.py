'''
토마토

N행 M 열

한칸에 하나의 토마토


1 은 익은 토마토
0 은 익지 않은 토마토
-1 은 없는칸

토마토가 하나 이상 있는 경우만 입력으로 주어진다.


'''
from collections import deque
import sys

M, N = map(int,sys.stdin.readline().split())

apple_box = [list(map(int,sys.stdin.readline().split())) for i in range(N) ]

# 1의 좌표 찾기
que = deque([])
for i in range(N):
    for j in range(M):
        if apple_box[i][j] == 1:
            que.append([i,j])
        
# 0이 한개도 없다면
# if not que:
#     print(0)

# # 0 이 존재한다면
# else:
    # 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일자 수 카운트
count = 0

while que:
    x,y = que.popleft()
    # 4방향
    for n in range(4):
        cx = x + dx[n]
        cy = y + dy[n]
        # 범위를 벗어나지 않고, 방문한 적이 없으며, -1 이 아닌곳
        if 0 <= cx < N and 0 <= cy < M and apple_box[cx][cy] == 0:
            apple_box[cx][cy] = apple_box[x][y] + 1
            que.append([cx,cy])

for i in range(N):
    if 0 in apple_box[i]:
        print(-1)
        exit()
    
    count = max(count, max(apple_box[i]))
# print(apple_box)
print(count-1)


                    


                    

