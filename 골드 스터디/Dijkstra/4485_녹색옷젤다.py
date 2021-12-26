'''
젤다전설  - 화폐 : 루피
$ 도둑루피 -- > 소지한 루피 감소

지금 도둑 루피만 가득한 N x N 크기의 동굴 제일 왼쪽위 --> 0,0

N-1,N-1까지 이동해야함

돈 손실을 최소화 + (상하좌우 1칸씩이동)

2차원 + 최소거리(비용)--> 다익스트라

'''
import heapq

def daik():
    q = []
    cost = [[INF]*N for _ in range(N)]
    heapq.heappush(q,[arr[0][0],0,0])
    cost[0][0] = 0

    while q:
        c,x,y = heapq.heappop(q)

        # 최단거리 우선이기때문에, 먼저 구해짐
        if x == N-1 and y == N-1:
            print("Problem {}: {}".format(count, c))
            break

        # 좌표별 순회 + q에 추가
        for i in range(4):
            cx,cy = x+dx[i],y+dy[i]
            # 범위초과 안한다면
            if 0<= cx < N and 0 <= cy < N:
                nc = c + arr[cx][cy]
                if nc < cost[cx][cy]:
                    cost[cx][cy] = nc
                    heapq.heappush(q, [nc,cx,cy])

INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 1
while True:

    N = int(input())

    if N == 0:
        break
    
    # 가중치 리스트
    arr = [list(map(int,input().split())) for _ in range(N)]

    daik()

    count += 1

