'''

총 12개의 가능성
가로 5 세로 5 대각 2

인덱스 지정
가로 0 1 2 3 4

세로 0 1 2 3 4

대각 0 1
 0 i ==j
 1 i+j = 4
'''


import sys
sys.stdin = open('input.txt')

numbers = [list(map(int, input().split())) for _ in range(5)]
# print(numbers)

yumi_x = []
garo = [0]*5
sero = [0]*5
king_gak_sun = [0,0]
bingo = 0
for i in range(5):
    yumi_x += list(map(int, input().split()))

for num in range(len(yumi_x)):
    for i in range(5):
        for j in range(5):
            if yumi_x[num] == numbers[i][j]:
                garo[i] += 1
                sero[j] += 1
                if i == j:
                    king_gak_sun[0] += 1
                if i+j == 4:
                    king_gak_sun[1] += 1

                if garo[i] == 5:
                    bingo += 1
                    garo[i] = 0
                if sero[j] == 5:
                    bingo += 1
                    sero[j] = 0
                if king_gak_sun[0] == 5:
                    bingo += 1
                    king_gak_sun[0] = 0
                if king_gak_sun[1] == 5:
                    bingo += 1
                    king_gak_sun[1] = 0

                if bingo >= 3:
                    result = num + 1
                    print(result)
                    exit()
                    # print(garo, sero, king_gak_sun)



