'''
회전이 된 사각형은 없다.
색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
'''

'''
가로세로 각각 크기가 10 인 정 사각형

3 13 10칸

2중 for문으로 칠해진 자리 1로 바꿔주기

3, 7 -- 인덱스 번호 3-13 까지 range(n, n+ 11) 
'''

N = int(input())

# 가로세로 100 인 정사각형 모양
visited = [[0]*101 for _ in range(101)]
# print(visited)


# 3가지 경우를 돌리겠다
for n in range(N):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            visited[j][i] = 1
count = 0
for i in range(101):
    for j in range(101):
        if visited[j][i] == 1:
            count += 1

print(count)