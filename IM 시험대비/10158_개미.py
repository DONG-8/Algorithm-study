'''
0 : 가로
1 : 세로

직사각형의 최대 넓이 구하기

N: 가로 M : 세로
자르는 횟수

0 3
1 4
0 2

0 2 3 ...., N
0, 4, ... , M
'''


N, M = map(int,input().split())

T = int(input())

garo = [0]
sero = [0]
for t in range(T):
    huhuhu = list(map(int, input().split()))

    if huhuhu[0] == 1:
        sero.append(huhuhu[1])
    else:
        garo.append(huhuhu[1])

garo.sort()
sero.sort()
garo.append(M)
sero.append(N)

# print(garo, sero)

garo_max = 0
sero_max = 0
for i in range(len(garo)-1):
    if garo[i+1] - garo[i] >= garo_max:
        garo_max = garo[i+1] - garo[i]

for j in range(len(sero)-1):
    if sero[j+1] - sero[j] >= sero_max:
        sero_max = sero[j+1] - sero[j]

# print(garo_max,sero_max)
result = garo_max*sero_max
print(result)





