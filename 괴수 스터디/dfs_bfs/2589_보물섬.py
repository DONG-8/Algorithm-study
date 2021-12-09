'''
# 육지  L
# 바다 W

한칸이동 1시간
육지로만 가능 >> 여기서 dfs로 풀어야겠다고 생각

근데 읽어보니까 아니였네?

최단거리를 구하기 때문에 bfs 로 모든 지점을 순회 돌려야함

방문처리를 위한 visit
근데 한번 싸이클이 끝나면 다시 방문처리 초기화

why? 각 지점에처 끝점의 거리를 매번 체크 그리고 그 시간을 갱신

어디 좌표를 알 필요는 없음

가지치기는 어떻게? 근데 최대를 구하는데 이 가지치기라는게 필요할까?

'''
# 시간복잡도 O(1) 이라는 장점을 이용하자
from collections import deque

# 밖에서 초기 que 값 입력받고 내부에서는 pop 이후 모든 과정 진행
def bfs(count):

    while que:
        
        count += 1
        # 한 단계 전진
        for i in range(len(que)):
            # 좌표 받기
            x, y = que.popleft()
            visit[x][y] = 1
            for distance_num in range(4):
                cx = x + dx[distance_num]
                cy = y + dy[distance_num]
                # 범위 내에 있고, L : 땅덩어리 이면서, 방문하지 않았던 장소라면
                if 0 <= cx < N and 0 <= cy < M and water_land_list[cx][cy] == "L" and visit[cx][cy] == 0:
                    # 방문처리를 해주고
                    visit[cx][cy] = 1
                    que.append([cx,cy])

    # 시간복잡도가 땡겨질런지    
    return count

N, M = map(int, input().split())
# N --> 행
# M --> 열

# 지역정보 받아오기
water_land_list = [input() for _ in range(N)]

# 생각해보니까 각 값을 입력할게 아니라 방문처리한 것만 불릴 때 마다 초기화
# 카운트만 늘려서 종료 됐을 때 카운트를 반환

# 벽을 세울 필요는 없다 방문할 수 있는 조건은
# L 이고 인덱스 범위에 존재한다면 이동하도록 한다

# 방향벡터

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대길이 갱신을 위한 변수 할당
max_length = 0

for i in range(N):
    for j in range(M):
        que = deque()
        if water_land_list[i][j] == 'L':
            visit = [[0]*M for _ in range(N)]
            que.append([i,j])
            a = bfs(0)
            if max_length < a:
                max_length = a

                
print(max_length-1)

