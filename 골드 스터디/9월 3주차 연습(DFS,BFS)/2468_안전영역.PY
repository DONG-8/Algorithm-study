'''
입력받기


'''
import sys
sys.stdin = open('test.txt')

import sys
sys.setrecursionlimit(100000)


n = int(input())

num_list = [list(map(int, input().split())) for _ in range(n)]

# print(num_list)

# 영역에서 가장 큰 높이 구하기
big_water = 0 
for i in range(n):
    a = max(num_list[i])
    if a >= big_water:
        big_water = a

# 갈 수 있는 영역을 탐색하기위한 dfs 지정
def dfs(x,y):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    cant_visit[x][y] = 1
    for k in range(4):
        change_x = dx[k] + x
        change_y = dy[k] + y
        if 0<= change_x < n and 0<= change_y < n and cant_visit[change_x][change_y] == 0:
            dfs(change_x,change_y)

max_Area = 0
for i in range(0,big_water+1):
    # 높이가 i 일때
    # 방문처리를 위한 리스트 생성
    cant_visit = [[0]*n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if num_list[x][y] <= i:
                cant_visit[x][y] = 5


    for x in range(n):
        for y in range(n):
            if cant_visit[x][y] == 0:
                dfs(x,y)
                count += 1

    if max_Area <= count:
        max_Area = count

print(max_Area)



            
            
                



    # 이미 찾은 영역이라면 지나가고 찾지 않은 영역이라면 체크할 수 있도록
    # 다 체크한 후 count에 1을 더해줌
    # 마무리 된 카운트를 갱신하기위한 최대 갯수 비교
    

