


import sys
sys.stdin = open('test.txt')


N, M = map(int,input().split())

chk = [list(map(int, input().split())) for i in range(N)]

# print(chk)

# 각 치킨집의 위치좌표 알아내기
# 각 집의 위치 알아내기

chicken = []
house = []

for i in range(N):
    for j in range(N):
        # 만약 좌표값이 2라면, 치킨좌표로 추가
        if chk[i][j] == 2:
            chicken.append([i, j])

        # 만약 좌표값이 1이라면, 집좌표로 추가
        if chk[i][j] == 1:
            house.append([i, j])

# print(chicken, house)
# [[1, 2], [2, 2], [4, 4]] [[0, 2], [1, 4], [2, 1], [3, 2]]

final_load = []
for x, y in chicken:
    ls = []
    for h1,h2 in house:
        length = abs(x-h1) + abs(y-h2)
        ls.append(length)
    final_load.append(ls)

# print(final_load)

arr = []
final = []
visit = []

def find_min(arr):
    result = [99] * len(house)

    for i in arr:
        for j in range(len(house)):
            if final_load[i][j] <= result[j]:
                result[j] = final_load[i][j]

    final.append(sum(result))
    return

def recur(cur,start):
    if cur == M:
        find_min(arr)
        print(arr)
        return

    for i in range(start,len(chicken)):
        arr.append(i)
        recur(cur+1,i+1)
        arr.pop()


recur(0,0)
print(min(final))