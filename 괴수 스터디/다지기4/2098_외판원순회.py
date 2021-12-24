'''
외판원 순회
갈 수 있는 순회경로만 진행된다.
한번 갔던 도시로는 다시갈 수 없다 -- > 맨 마지막에 여행을 출발했던 도시로 돌아오는것은 예외
도시간 이어지지 않은 경우도 있다.

'''
def recur(start, cnt, num):
    global minimum
    
    # 가지치기
    if num > minimum:
        return
    # 마지막 갈 지점은 0행으로 가야하기 때문에 0열으로 고정!
    # 따라서 그 전까지 경로 받은 후 마지막 은 start지점의 0행의 cost를 더해주면
    # 순회경로 완성!
    if cnt == N-1:
        if arr[start][0] != 0:
            num += arr[start][0]
            if num < minimum:
                minimum = num
        return
    # 0 제외 순회
    for k in range(1,N):
        if arr[start][k] != 0 and visit[k] == 0:
            visit[k] = 1
            recur(k,cnt+1,num + arr[start][k])
            visit[k] = 0


# 입력

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# print(N, arr) 4 [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

# 외판원 순회는 어느 점에서 시작하던지, 결국 출발점으로 돌아와야한다.
# 이 말은 한 특정 지점을 시작점을 잡고 다시 지점으로 돌아오게하는 백트래킹 기법을 사용하면 풀 수 있는 문제이다.

# 시작점은 열을 기준 0,1 이면 0 -> 1 로 가는 경우이다.
# 그럼 다음 지점은 1 -> ?? 이기 때문에 0열은 제외하고 찾아야한다.
# 왜냐하면 0열은 시작지점이기때문에 다시 돌아와야하므로 탐색 대상에서 제외되어야한다.
# 그리고, 방문하게 된 곳을 방문처리!

# 그렇다면 방문처리를 위한 list는 행을 기준 도착점은 다시 도착점에 해당하는 열을 찾아야한다
visit = [0]*N
minimum = int(1e9)
# 시작점은 0 ->> 아무마을 단 값이 0이 아닌마을로
# 자기자신으로 갈 수 없으니 범위는 1부터 n-1까지
for i in range(1,N):
    # 0인 지점 안지나게
    if arr[0][i] != 0:
        visit[i] = 1
        # 도착한 곳의 경로정보,종료조건 == cnt,0->  ?? 로 가는 cost
        recur(i,1,arr[0][i])
        visit[i] =  0

print(minimum)

# 1트라이 시간초과
