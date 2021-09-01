'''

기울어진 색종이는 없다.
순서대로 위에 덮어 씌우는 과정
그렇다면 첫번째 색종이는 1번
두번째 색종이는 2번.. 이런식으로 증가 시킨 후
마지막 이중 for문을 통해, 각 숫자를 카운트
변수는 갯수에 맞게 증가 시킨다.
길이에 상관없이 구하고 싶다면 비어있는 인덱스를 만들어서
값을 추가 해 주는 방법으로 한다.

'''

import sys
sys.stdin = open('input.txt')

# N = int(input())
#
# # 빈 격자 생성
#
# # 1001칸은 0~ 1000 까지
# zero = [[0]*1001 for _ in range(1001)]
#
# # 색종이가 발견되지 않는 경우를 위한 0 대입
# # 이후에는 인덱스 번호로 접근
#
# # 칸 색칠
# for i in range(1, N+1):
#     x1, y1, w, h = map(int, input().split())
#     for g in range(x1, x1+w):
#         for s in range(y1, y1+h):
#             zero[g][s] = i
# ls = [0]
# for ff in range(1, N+1):
#     a = 0
#     for k in range(len(zero)):
#         a += zero[k].count(ff)
#     ls.append(a)
#
#
# for n in range(1,len(ls)):
#     print(ls[n])



N = int(input())

if 1 <= N <= 10:
    zero = [[0]*101 for _ in range(101)]
else:
    zero = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
    x1, y1, w, h = map(int, input().split())

    for g in range(x1, x1+w):
        for s in range(y1, y1+h):
            zero[g][s] = i

for ff in range(1, N+1):
    a = 0
    for k in range(len(zero)):
        a += zero[k].count(ff)
    print(a)


