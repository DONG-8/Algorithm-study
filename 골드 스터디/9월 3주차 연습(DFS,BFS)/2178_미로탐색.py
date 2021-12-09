
'''
n m
n 행 m 열

1,1 출발
n,m 도착지

최단거리문제기 때문에 bfs 이다.
'''

import sys
sys.stdin = open('test.txt')

n, m = map(int, input().split())


# 붙어서 입력되기 때문에 구분지어준다.
miro = []
for i in range(n):
    ls = []
    xx = input()
    for j in xx:
        ls.append(int(j))

    miro.append(ls)

# 데이터 입력 끝

# 최단거리 문제이기 때문에 bfs 를 이용한다.
# 방문 체크를 위한 리스트
visit = [[0]*m for _ in range(n)]
# print(visit)

# 시작지점
x, y = 0, 0
que = [[x,y]]
count = 0
# 방문처리
visit[x][y] = 1
while que:
    size = len(que)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(size):
        a = que.pop(0)
        if a[0] == n-1 and a[1] == m-1:
            print(count+1)
            exit()


        for j in range(4):
            cx = a[0] + dx[j]
            cy = a[1] + dy[j]
            if 0<= cx < n and 0 <= cy < m and miro[cx][cy] ==1 and visit[cx][cy] ==0:
                visit[cx][cy] = 1
                que.append([cx,cy])
    count += 1


