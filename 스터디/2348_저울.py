'''

1 2 3 8


'''

import sys
sys.stdin = open('test.txt')

n = int(input())

num = list(map(int, input().split()))

num.sort()
result = num[0]

if n == 1:
    if num[0] == 1:
        print(2)
    else:
        print(1)

elif n >= 2:
    for i in range(1, n):
        if num[0] != 1:
            print(1)
            break

        if num[i] - result <= 1:
            result += num[i]
        else:
            result += 1
            print(result)
            break
    else:
        print(result + 1)

#
# weight = 1
# for i in range(n):
# 
#     if weight < num[i]:
#         break
#
#     weight += num[i]
#





