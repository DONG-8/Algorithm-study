'''

입력
5
1 3 2 4 6
2 7 3 4 1

이걸 어떻게 위 아래 묶어서 받지?


'''

# import sys
# sys.stdin = open('test.txt')
#
# N = int(input())
#
# first = list(map(int, input().split()))
#
# grow = list(map(int, input().split()))

# print(first, grow)

# 인덱스 값끼리 연결된 특성을 이용하여 정렬시켜준다.
# for i in range(N):
#     for j in range(N-1):
#         if grow[j] > grow[j+1]:
#             grow[j], grow[j+1] = grow[j+1], grow[j]
#             first[j], first[j+1] = first[j+1], first[j]

# print(first, grow)
# result = 0
# for i in range(N):
#     result += i*grow[i] + first[i]
#
# print(result)

import sys
sys.stdin = open('test.txt')

N = int(input())

first = list(map(int, input().split()))

grow = list(map(int, input().split()))

grow.sort()

sum = sum(first)

for i in range(N):
    sum += i*grow[i]

print(sum)



