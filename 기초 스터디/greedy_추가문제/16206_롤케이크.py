'''
롤케이크

N명에게 롤케이크 1개씩 선물로 받았다.
롤케이크의 길이는 A1, A2, ..., AN

재현이는 길이가 10인 롤케이크만 먹는다
--> 까다로운녀석이구만

10인 롤케이크를 최대한 많이 만들려고 한다.

10 넘어가는거만 가능하지않나?

자를 롤케이크를 하나 고른다. 길이가 1보다 큰 롤케이크만 자를 수 있다. 이때, 고른 롤케이크의 길이를 x라고 한다.
0보다 크고, x보다 작은 자연수 y를 고른다.
롤케이크를 잘라 길이가 y, x-y인 롤케이크 두 개로 만든다.

재현이는 롤케이크를 최대 M번 자를 수 있다
'''

'''
입력
3 1
10 10 10

출력
3


입력

3 1
10 10 20

출력

4
'''

import sys
sys.stdin = open('test.txt')

N, M = map(int, input().split())
ls = list(map(int, input().split()))

# 10 이면 그냥 카운트 증가
# 10보다 크면 -10

# 순서대로 탐색하면 문제 발생
# 10인것들은 미리 제거 후 시작

count = 0
# for i in range(N):
#     if ls[i] == 10:
#         count += 1
#         ls[i] -= 10
#
# a = ls.count(0)
# for i in range(a):
#     ls.remove(0)
#
# if not ls:
#     print(count)
#     exit()
# else:
#     i = 0
#     while i < len(ls) and M > 0:
#         if ls[i] > 10:
#             M -= 1
#             ls[i] -= 10
#             count += 1
#
#         if ls[i] == 10:
#             count += 1
#             i += 1
#         elif ls[i] < 10:
#             i += 1
# print(count)

for i in range(N):
    if ls[i] == 10:
        count += 1
        ls[i] -= 10

a = ls.count(0)
for i in range(a):
    ls.remove(0)

ls.sort()
baesoo = []
notbaesoo = []
for i in range(len(ls)):
    if ls[i]%10 == 0:
        baesoo.append(ls[i])
    else:
        notbaesoo.append(ls[i])

ls = baesoo + notbaesoo
i = 0
while i < len(ls) and M > 0:

    if ls[i] > 10:
        M -= 1
        ls[i] -= 10
        count += 1

    if ls[i] == 10:
        count += 1
        i += 1
    elif ls[i] < 10:
        i += 1
print(count)







