'''
점수 획득
순위 매기기 - > 정렬

특정 레벨의 점수를 감소시키려고 한다.

구하고자 하는 값

점수들을 몇번 감소시키면 될까?

레벨별로는 점수가 증가해야함 '오름차순'

점수 내리는걸 최소한으로 만들어 준다.

'''

import sys
sys.stdin = open('test.txt')

# 레벨의 갯수!
N = int(input())

score_list = [int(input()) for _ in range(N)]

# print(score_list)

score_list = score_list[-1::-1]
# print(score_list)

count = 0
bibigo_king = score_list[0]

i = 1
while i < N:
    if bibigo_king <= score_list[i]:
        score_list[i] -= 1
        count += 1
        if score_list[i] < bibigo_king:
            bibigo_king = score_list[i]
            i += 1
    else:
        bibigo_king = score_list[i]
        i += 1


print(count)

