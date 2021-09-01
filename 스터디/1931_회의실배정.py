'''
회의실 배정

N 개의 회의에 대하여 회의실 사용 표를 만들려고 한다.
각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 갯수 찾기

---- 입력

첫째 줄에 회의의 수  N 이 주어진다. 둘째 줄 부터 N+1 줄까지 각 회의의
정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작과 끝나는 시간이 주어진다
시작시간과 끝나는 시간은 2**31-1 보다 작거나 같은 자연수이다.

 >> 즉 범위가 너무 많기 때문에 완탐으로 풀면 시간제한에 걸린다.

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

 ---- 출력

 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

4
'''

# 입력을 받는다

N = int(input())

clock = [list(map(int,input().split())) for i in range(N)]

# print(clock)

clock.sort(key = lambda x : (x[1],x[0]))
# print(clock)

i = 0 # idx
# 제일 처음 clock[0][1] 은 회의 종료 시간
# 이 종료시간과 가장 가까운 회의 시작 시간을 찾는다
count = 1 # 이미 첫번째부터 시작이 된거기 때문에 count = 1
start_time = clock[0][1]
for j in range(1,N):
    if clock[j][0] >= start_time:
        start_time = clock[j][1]
        i = j
        count += 1
        

print(count)
    

    