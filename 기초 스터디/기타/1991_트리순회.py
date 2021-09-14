'''
이진트리는 2가지로 나뉘어진다.
따라서 처음 받은 인자를 왼쪽 으로
두번째 받은 인자를 오른쪽 인자로 보내준다.
'''


import sys
sys.stdin = open('test.txt')

def center_order(n=1):
    if n:
        center_order(start_point.index(lf[n]))
        print(start_point[n], end='')
        center_order(start_point.index(ri[n]))


def first_order(n=1):
    if n:
        print(start_point[n], end='')
        first_order(start_point.index(lf[n]))
        first_order(start_point.index(ri[n]))


def last_order(n=1):
    if n:
        last_order(start_point.index(lf[n]))
        last_order(start_point.index(ri[n]))
        print(start_point[n], end='')



N = int(input())
lf = [0]*(N+1)
ri = [0]*(N+1)
start_point = [0]*(N+1)
for j in range(1,N+1):
    en_ls = list(input().split())
    for i in range(3):
        if i == 0:
            start_point[j] =en_ls[i]
        if en_ls[i] == '.':
            continue

        if i == 1:
            lf[j] = en_ls[i]
        if i == 2:
            ri[j] = en_ls[i]

first_order()
print()
center_order()
print()
last_order()



# print(start_point, lf, ri)
# # #[0, 'A', 'B', 'C', 'E', 'F', 'D', 'G']
# # #[0, 'B', 'D', 'E', 0, 0, 0, 0] [0, 'C', 0, 'F', 0, 0, 0, 0]
# #
# # print(lf[1])
# # print(start_point.index(lf[1]))
# # center_order(2)
# print(start_point.index(lf[3]))
