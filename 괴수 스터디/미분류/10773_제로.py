


import sys
sys.stdin = open('test.txt')

N = int(input())

result = []
for n in range(N):

    num = int(input())

    if not num:
        result.pop()

    else:
        result.append(num)


print(sum(result))
