

import sys
sys.stdin = open('test.txt')

N = int(input())

too_p = [int(input()) for _ in range(N)]

ls = too_p[1:N]
count = 0
while ls:
    # 종료조건
    if max(ls) < too_p[0]:

        break

    else:
        ls[ls.index(max(ls))] -= 1
        too_p[0] += 1
        count += 1

print(count)