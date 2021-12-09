'''
적록 색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.


'''
from collections import deque


def bfs(colorls,xp,yp,visite):   
    q = deque()
    q.append([xp,yp])
    visite[xp][yp] = 1
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    while q:
        x,y = q.popleft()
        color = colorls[x][y]
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < N and color == colorls[cx][cy] and visite[cx][cy] == 0:
                visite[cx][cy] = 1
                q.append([cx,cy])

def find_area(list_of_color):
    visite = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visite[i][j] == 0:
                bfs(list_of_color,i,j,visite)
                cnt += 1
    return cnt


# 입력
N = int(input())

color_list = [ ]
gr_same_list = []
for _ in range(N):
    spell = input()
    ls = []
    ch = []
    for i in spell:
        ls.append(i)
        if i == "G":
            i = "R"
        ch.append(i)


    color_list.append(ls)
    gr_same_list.append(ch)
# 색깔별 구별, 색록 => 빨,초 같은색으로 인식
# print(color_list)
# print(gr_same_list)
print(find_area(color_list))
print(find_area(gr_same_list))



