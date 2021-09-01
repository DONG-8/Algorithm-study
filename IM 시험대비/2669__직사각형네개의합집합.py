'''
회전한 사각형은 없다.

겹치거나 뭐 어쨋든 여러개 중복이 가능하다.
차지하는 면적을 구해라
'''

# 가로세로 100 인 정사각형 모양
visited = [[0]*101 for _ in range(101)]
# print(visited)


# 3가지 경우를 돌리겠다
for n in range(4):
    x, y, x1, y1 = map(int, input().split())
    for i in range(x,x1):
        for j in range(y,y1):
            visited[j][i] = 1
count = 0
for i in range(101):
    for j in range(101):
        if visited[j][i] == 1:
            count += 1

print(count)