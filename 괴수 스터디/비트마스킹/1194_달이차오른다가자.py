from collections import deque

# 입력받기
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
x,y = 0,0
for i in range(N):
    a = input()
    for j in range(len(a)):
        arr[i].append(a[j])
        if a[j] == "0":
            x = i
            y = j

#
# 키를 들고 방문 한 경우까지 추가해서 visit 배열을 만들어준다.

# 키를 가지고 안가지고에 대한 경우의 수 2^6 표현
visit = [[[0 for _ in range(1<<6)] for j in range(M)] for i in range(N)]
# print(visit)

door = ['A','B','C','D','E','F'] # 인덱스 번호로 접근 0부터 시작
door_key = ['a','b','c','d','e','f'] # 0 부터 시작 연결하는 key 값은 index 번호

# bfs -> 최단거리  + 키를 가지고 있는지 없는지를 bit를 이용해서 풀어준다.

def bfs(start_x,start_y):
    # print(start_x,start_y)
    q = deque()
    q.append((start_x,start_y,0,0))
    # 아무런 키 없이 시작하기에, 0번 방문처리, 키를 가지고 다시 원점을 갈 수 있음.
    visit[start_x][start_y][0] = 1
    arr[start_x][start_y]  = "."
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        
        mx,my,dis,key = q.popleft()
        
        if arr[mx][my] == '1':
            
            return dis


        for i in range(4):
            # 이동 할 좌표
            nx = dx[i] + mx
            ny = dy[i] + my
            # 벽이 아닐때
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '#' and visit[nx][ny][key] == 0:
                # print('들어옴')
                if arr[nx][ny] == '.':
                    # 어? 여기도 키 상황이 들어가야하는디..? 어디서 가져오지?
                    # --> 이 단계에서 key값 추가
                    visit[nx][ny][key] = 1
                    q.append((nx,ny,dis + 1, key))
                    
                
                elif arr[nx][ny] == '1':
                    return dis + 1
                else:
                    if arr[nx][ny] in door:
                        # bit 를 이용하여, 해당 키를 가지고 있다면,
                        
                        
                        if key & (1 << door.index(arr[nx][ny])):
                        
                            visit[nx][ny][key] = 1
                            q.append((nx,ny,dis + 1, key))
                    elif arr[nx][ny] in door_key:
                        # bit
                        # 가지고있던 key에 현재 방문한 곳의 key를 추가해줌
                        nkey = key | (1 << door_key.index(arr[nx][ny]))
                        # 현재까지 거쳐온 키와, 이동 할 위치의 키를 가지고 방문한 기록이 없다면
                        if visit[nx][ny][nkey] == 0:
                            visit[nx][ny][nkey] = 1
                            # 방문처리
                            q.append((nx,ny,dis+1,nkey))
                    
                        
    return -1

        

print(bfs(x,y))





''' 
# 메모이제이션
# dp =[[-1 for _ in range(1 << M)] for _ in range(N)]
my_key = []


def recur(x,y):
    # # 종료조건
    # # 도착한거리라면 0을 리턴
    # if arr[x][y] == 1:
    #     return 0

    # # 이미 이동해왔던 경로라면 dp return
    # # ..? key를 가지고있을때는 어케할거?
    # # 키도 여러개 들고있을텐데..? 그때에 따라 달라질 수 있지않나?
    # # dp는 불가

    q = deque()
    q.append((x,y,0))


    # 이동벡터
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    way = 1e9

    # 이동해봐
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and  arr[nx][ny] != "#":
                
            if arr[nx][ny] == ".":
                # 길이면 가야지!
                print('gm')
            elif arr[nx][ny] in door:
                print('문')
            elif arr[nx][ny] in key:
                print('키')

# recur(x,y,my_key)


'''
