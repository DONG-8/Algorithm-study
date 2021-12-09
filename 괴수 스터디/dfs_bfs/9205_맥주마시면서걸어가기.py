'''

출발은 상근이네집,

한칸에 1미터

맥주 20개 들고 있음

편의점 방문시 맥주 다시 20개

-32768 <= x,y <= 32768


2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000


1
2
0 0
1000 0
2000 1000
2000 2000

'''
# dfs! : 그냥 갈 수 있으면 되는거니까 대신 방문한곳은 방문처리
# global 변수 하나로 도착하면 1 아니면 그대로 return 되도록 처리하면 도착했는지 안했는지 확인할 수 있다.

def dfs(x,y):
    global result
    
    # 불러진 x,y 좌표가 마지막 페스티벌 장소라면? 종료하세요
    if x == list_of_xy[-1][0] and y == list_of_xy[-1][1]:
        result = 1
        return

    else:
        # 아니라면?
        for i in range(len(go_to_festival)):
            # 각 좌표를 불러온다.
            # 만약 현재의 값과 받아온 좌표의 거리가 1000 보다 작으면 그리고 들렀던 곳이 아니라면 
            if abs(go_to_festival[i][0]-x)+ abs(go_to_festival[i][1]-y) <= 1000 and visit[i] == 0:
                # 방문처리
                visit[i] = 1
                # 그럼 다른 좌표를 찾아볼까?
                print(visit,i,'번째 좌표를 편의점을 방문했습니다.')
                dfs(go_to_festival[i][0],go_to_festival[i][1])

            # 거리 미달이라면? 일단 다른 경로 찾아보게 해야함
            # 다른 조건이 있나?
            # 없네


# 테스트케이스
T = int(input())

for t in range(T):

    # 편의점 수n
    n = int(input())
    # n+2 개의 줄에 상근이네집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 
    list_of_xy = []
    for i in range(n+2):
        list_of_xy.append(list(map(int,input().split())))
    

    # ------------------------ 위까지 input ---------------------------------- #
    # 모든 좌표를 방문 할 필요는 없다.

    # 거리 절대값을 구해서, 이 거리가 50*20 1000 이 안된다면 바로 실패
    # 아니면 또 진행 편의점 위치, 들린곳은 방문처리

    x, y = list_of_xy[0][0], list_of_xy[0][1]

    go_to_festival = list_of_xy[1:]
    
    # 방문 처리를 위한 리스트
    visit = [0]*len(go_to_festival)
    # print(go_to_festival)
    result = 0
    dfs(x,y)
    
    if result:
        print('happy')
    else:
        print('sad')
