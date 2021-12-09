'''
두묶음의 숫자카드

A,B 는 각 묶음의 카드 숫자
두묶음을 합쳐서 하나로 만드는데에는 A+B번의 비교를 해야한다.

이때 어떤 방식으로 묶냐에따라 효율이 달라지는데 어떻게 하면 최소 비교횟수를 알 수 있을까?
'''

# N = int(input())

# card = []
# for i in range(N):
#     card.append(int(input()))

# print(card)

# 어떻게 묶어야만 효율적인 카드 비교가 나올 수 있을까?

'''
비교군

10 20 40

10 40 40 60 

매번 정렬을 시켜주어서 최소한의 합을 만들어주는것이 관건임

'''

# if len(card) == 1:
#     print(0)
# else:
#     card.sort()
#     tot = 0
#     count = 0
#     while count < N-1:
#         count += 1
#         a = card.pop(0)
#         b = card.pop(0)
#         hap = a + b
#         tot += hap
#         card.append(hap)
#         card.sort()
#     print(tot)

#------------------------------------------

import heapq

N = int(input())

card = []
for i in range(N):
    heapq.heappush(card, int(input()))

if len(card) == 1:
    print(0)
else:
    count = 0
    tot = 0
    while count < N-1:
        count += 1
        a = heapq.heappop(card)
        b = heapq.heappop(card)
        num = a + b
        tot += num
        heapq.heappush(card, num)

    print(tot)