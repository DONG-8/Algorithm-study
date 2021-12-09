
import heapq

# 시작점과 끝점을 입력받을것임
def daiks(start,end):
    # 빈 리스트 생성
    que = []

    # 각 구간별 최대값 비교를 위한 값 생성
    INF = int(1e9)

    way_to_time = [INF for _ in range(n+1)]
    
    # 문제의 조건을 살펴보자, 최단시간에 오고가길 원한다.
    # 결국 모든길을 탐색해서 최단거리를 탐색해야한다.
    # INF인 경우는 없는가? : 문제의 입력조건에 존재한다.

    # 시작지점 가중치 0으로 만들기
    way_to_time[start] = 0
    heapq.heappush(que, [0,start])
    # 시작점입력 초기는 0 에서 시작점으로 이동

    # que 가 존재할 때 까지
    while que:

        time, goto = heapq.heappop(que)

        if time > way_to_time[goto]:
            continue

        for i in way[goto]:
            change_time = i[0] + way_to_time[goto]
            if change_time < way_to_time[i[1]]:
                way_to_time[i[1]] = change_time
                heapq.heappush(que, [change_time,i[1]])

    return way_to_time[end]

# 왔다 갔다를 알아야함
#  n 정점, m 간선, x 파티 위치
n, m, x = map(int,input().split())
way = [[] for _ in range(n+1)]

for i in range(m):
    s,e,t = map(int,input().split())

    way[s].append([t,e])


# way : [[], [[4, 2], [2, 3], [7, 4]], [[1, 1], [5, 3]], [[2, 1], [4, 4]], [[3, 2]]]

# 오고 가는 시간 : 1 - > 2 2 -> 1로 가는 시간
# 시작점이 1일때 end의 값, 시작점이 2일 때 start point 의 인덱스 값 2가지가 있다.
# 함수화 시키고  for문을 통한 반복으로 최대값 갱신 result에결과 할당 종료

# 가장 큰 값 도출
result = 0
for i in range(1,n+1):
    if i == x:
        continue

    a = daiks(i,x)
    b = daiks(x,i)
    person_time = a + b
    if person_time > result:
        result = person_time

print(result)



    