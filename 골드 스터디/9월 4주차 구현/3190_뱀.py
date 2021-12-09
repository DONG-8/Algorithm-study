

import sys
sys.stdin = open('test.txt')

N = int(input())
# 배열생성 시작점이 1,1 이기 때문에 좌표에 맞게 생성시켜준다
Dummy = [[0]*(N+2) for i in range(N+2)]

# 사과갯수
apple_number = int(input())

for _ in range(apple_number):
    x, y = map(int,input().split())

    Dummy[x][y] = 2

for i in range(N+2):
    Dummy[0][i] = 1
    Dummy[i][0] = 1
    Dummy[i][N+1] = 1
    Dummy[N+1][i] = 1

# 벽 1로 전환
# print(Dummy)

# 방향 변환 횟수

turn = int(input())

# 처음 방향변환할 좌표가 turn_direction[0] 에 들어가 있다.
turn_direction = []
for _ in range(turn):
    # 몇초뒤 방향전환, 전환 할 방향
    count_time, direction = input().split()
    turn_direction.append([count_time, direction])

# 첫 시작점

# 종료조건
# tail = head or 0>= head_x or head > N




# 방향전환 함수
# 뱀의 이동방향은 오른쪽
# L -> 왼쪽, D 오른쪽
def turn_dir(dir):
    global dx,dy

    if dx ==0 and dy == 1:
        if dir == 'D':
            dx, dy = 1,0
        else:
            dx, dy = -1,0
    elif dx == 0 and dy == -1:
        if dir == 'D':
            dx, dy = -1,0
        else:
            dx, dy = 1,0

    elif dx == 1 and dy == 0:
        if dir == 'D':
            dx, dy = 0,-1
        else:
            dx, dy = 0,1

    elif dx == -1 and dy == 0:
        if dir == 'D':
            dx, dy = 0,1
        else:
            dx, dy = 0,-1
    return dx,dy

# que 를 이용하여 좌표값 지속적으로 불러오기
# 조건에 따라 종료, 방향 전환 및 방문처리하기 크게 3가지의 분기점

# 종료조건
# 몸통이 있는곳, or 벽 모두 1로 처리했기 때문에 좌표가 1에 도달하면 종료

tail = [[1, 1]]


# 시작점 방문처리
Dummy[1][1] = 1
# Dummy[1][2] = 1

# print(Dummy)
# 처음 이동 방향 오른쪽
dx, dy = 0, 1

# 시간 카운트
time = 0
x, y = 1, 1
while True:
    time += 1
    cx = x + dx
    cy = y + dy

    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.

    # 현재 시간이 turn_direction첫번째 리스트의 0번 인덱스와 값이 같다면
    try:
        if int(turn_direction[0][0]) == time:
        # dx,dy를 변환 시킨 후 좌표값을 변환
            turn_dir(turn_direction[0][1])
            turn_direction.pop(0)
    except IndexError:
        pass

    if Dummy[cx][cy] == 1:
        print(time)
        exit()

    if Dummy[cx][cy] == 0:
        Dummy[cx][cy] = 1
        tail.append([cx, cy])
        a = tail.pop(0)
        Dummy[a[0]][a[1]] = 0
        x, y = cx, cy

    elif Dummy[cx][cy] == 2:
        Dummy[cx][cy] = 1
        tail.append([cx, cy])
        x, y = cx, cy







    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    # 초는 1번 이동에 1씩 증가









