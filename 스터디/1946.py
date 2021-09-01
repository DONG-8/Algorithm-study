# 1946 신입사원

import sys

T = int(sys.stdin.readline())
num = []
for t in range(T):
    ls = []
    a = int(input())
    for j in range(a):
        k = list(map(int, sys.stdin.readline().split()))
        ls.append(k)
    
    ls.sort()
    print(ls)
    count = 1
    mini = ls[0][1] # 초기 값
    for i in range(a):
        if mini > ls[i][1]:
            count += 1
            mini = ls[i][1]
    print(count)


#-----------------------------시간초과

    # count = 0
    # last_list = []
    # for i in range(a):
    #     for a, b in ls:
    #         if ls[i][0] > a and ls[i][1] > b:
    #             break
    #     else:
    #         count += 1
    #
    # print(count)

