'''

1번부터 N번 까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다.(없을수도 있다.)
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 
단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 
이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 
대칭 x


'''
# 1차 시도중 깨달아버림 (기존코드)
'''
# 재귀를 돌아보실까
# for i in range(N):
#     for j in range(N):
#         #패스조건
#         if i == j:
#             continue
#         # 방문한곳이면?
#         if visit[i] == 1 or visit[j] == 1:
#             continue

왜냐라고 질문을 한다면, 가는 방향을 맞춰서 그 행의 값을 찾아가야함
그렇기 때문에 재귀 호출에는 바라보는 행을 기입해서 그 행별로 방문처리를 해야할 필요성이 생김

'''
# 내려갔다가 다시 올라오기 --> 방문처리 해제 필수
# 거르는조건 2개
# 가지치기 --> 내부 조건문 말고는 생각안남 현재
# 한가지 중요 조건! --> 길이 없는 경우도 있음 & 


def recur(i,cnt,num):
    global mini_number
    
    # 가지치기
    if num > mini_number:
        return
    
    # 종료조건
    if cnt == N-1:
        if arr[i][0]:
            num += arr[i][0]
            if num < mini_number:
                mini_number = num
        return

    array_of_i = arr[i]
    for j in range(1,N):
        if array_of_i[j] and visit[j] == 0 :
            visit[j] = 1
            recur(j,cnt+1,num+array_of_i[j])
            visit[j] = 0

# 입력
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 최댓값 지정
mini_number = int(1e9)
# 생각해봅시다.
visit = [0]*N

# 방문처리는 행을 처리해줘야함
# 반복문을 통한 행의 처리
for j in range(1,N):
    if arr[0][j] != 0:
        visit[j] = 1
        recur(j,1,arr[0][j])
        visit[j] = 0


print(mini_number)
