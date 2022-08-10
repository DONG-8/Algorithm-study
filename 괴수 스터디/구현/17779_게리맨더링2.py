
def line(x,y,d1,d2):
    visit = [[0] * (N+1) for _ in range(N+1)]
    # d1 까지인 케이스 탐색
    for i in range(d1+1):
        visit[x + i][y - i] = 5
        visit[x+d2 + i][y+d2 - i] = 5

    # d2 까지인 케이스 탐색
    for j in range(d2+1):
        visit[x + j][y + j] = 5
        visit[x + d1 + j][y - d1 + j] = 5

    for k in range(x+1,x+d1+d2):
        five = False
        for z in range(1,N+1):
            if visit[k][z] == 5:
                five = not five

            if five == True:
                visit[k][z] = 5

    # print(visit)
    return visit

N = int(input())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0]*(N+1))
# 점의　좌표를　찍는것이　중요함
# for i in range(N+1):
#     print(arr[i])
coordinate = []
min_num = 1000000000000000000000000000000000

# 1. 범위를 만족하는 x,y좌표와 d1, d2를 구한다.
# 2. 경계선과 각 영역이 몇인지를 표시한다.
for i in range(1,N+1):
    for j in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                # 범위를 만족한다면 x,y 좌표와 이에 해당하는 경계선 길이를 arr에 추가
                if 1 <= i and i+d1+d2 <= N and 1 <= j-d1 < j  < j+d2 <= N :
                    # 경계영역을 나누어준다.
                    coordinate.append([i,j,d1,d2])


# print(coordinate)
while coordinate:

    x,y,d1,d2 = coordinate.pop()
    num_arr = [0,0,0,0,0,0]
    visit = line(x,y,d1,d2)
    # for _ in range(N+1):
    #     print(visit[_])
    # print('----------------------')
    for i in range(1,N+1):
        for j in range(1,N+1):
            # 어느영역인지 확인하고, 이에 따른 1,2,3,4,5 번 영역의 배열에 값 추가
            if visit[i][j] != 5:
                if i < x + d1 and j <= y:
                    num_arr[1] += arr[i][j]
                    visit[i][j] = 1
                elif i <= x+d2 and y < j <= N:
                    num_arr[2] += arr[i][j]
                    visit[i][j] = 2
                elif x + d1 <= i <= N and 0 <= j < y - d1 + d2:
                    num_arr[3] += arr[i][j]
                    visit[i][j] = 3
                elif x + d2 < i <=N and y-d1+d2 <= j <= N:
                    num_arr[4] += arr[i][j]
                    visit[i][j] = 4
            else:
                num_arr[5] += arr[i][j]

    # print('x와 y가' ,x,y,"일때" ,d1,d2,"임")
    # for k in range(N+1):
    #     print(visit[k])
    min_num = min(min_num,max(num_arr[1:]) - min(num_arr[1:]))

# 4,2 =>  0,1,1,4
print(min_num)