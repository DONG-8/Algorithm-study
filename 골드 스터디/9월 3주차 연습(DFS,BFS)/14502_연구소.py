'''

세울 수 있는 벽의 개수는 3개

크기 n m 연구소


영역 -> 0 의 갯수
n과 m의 범위가 작다.
그럼 2가 생기는 갯수를 카운트 --> 한번 끝난 후 최댓값 비교

1은 3개를 채워 줘야함  --> 어디에? 비어있는 자리에 0 이 있는 자리라면 1로 바꿔줌

'''


import sys
sys.stdin = open('test.txt')

# 좌표값 받기

n, m = map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))

max_Area = 0

# 1의 위치 3개를 바꿔 줘야함
# 바꿔 주었을 때 bfs를 실행시켜야한다.

# 0 의 좌표값을 받아와서 한다?

# 벽 선택
# 원본정보말고 복사한 정보를 가져야함
# 리스트 복사
copy = [[0]*m for _ in range(n)]

# 선택해진 벽 마다 다른 확장을 가지기 때문에
# 원본의 변화가 아니라 새로운 리스트가 필요함
# 비교하고 나서는 다른 벽을 선택할때 확장된 바이러스가 그대로 남으면 안됨
# 그렇기 때문에 리스트를 복사시켜줘야함

# bfs

def bfs():
    global max_Area

    for i in range(n):
        for j in range(m):
            copy[i][j] = num_list[i][j]

    que = []
    # 2를 만나면 0 혹은 범위 벗어날때까지 확장
    count = 0
    for xx in range(n):
        for yy in range(m):
            if copy[xx][yy] ==2:
                dx = [0,0,-1,1]
                dy = [-1,1,0,0]
                que.append([xx,yy])
                while que:
                    a = que.pop(0)
                    x = a[0]
                    y = a[1]
                    for k in range(4):
                        cx = x + dx[k]
                        cy = y + dy[k]
                        if 0 <= cx < n and 0 <= cy < m and copy[cx][cy] == 0:
                            copy[cx][cy] = 2
                            que.append([cx,cy])
    # 확장 후 0 찾기
    for x_zero in range(n):
        for y_zero in range(m):
            if copy[x_zero][y_zero] == 0:
                count += 1

    if max_Area <= count:
        max_Area = count


# 3개의 벽을 선택 --> 중복 없는 조합
def wallchoice(cnt):
    if cnt == 3:
        bfs()
        return

    for nn in range(n):
        for mm in range(m):
            if num_list[nn][mm] == 0:
                num_list[nn][mm] = 1
                wallchoice(cnt+1)
                # 하나의 선택이 되었다면 bfs 호출 후 다른벽을 선택할 수 있게 0으로 만들어줌
                num_list[nn][mm] = 0


wallchoice(0)
print(max_Area)




