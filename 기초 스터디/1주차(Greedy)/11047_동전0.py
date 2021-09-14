'''

'''

import sys
sys.stdin = open('test.txt')

N, num = map(int, input().split())
ls =[]

for i in range(N):
    ls.append(int(input()))

ls.sort(reverse=True)
count = 0
for i in range(N):
    if ls[i] <= num:
        while num >= ls[i]:
            num -= ls[i]
            count += 1
    if num == 0:
        break

print(count)
