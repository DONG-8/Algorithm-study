'''



'''

import sys
sys.stdin = open('input.txt')

N = int(input())

num = list(map(int, input().split()))
ls = []
# print(num)
count = 0
for i in range(len(num)-1):
    ls.append(num[i+1] - num[i])

# print(ls)
max_count = 0
for i in range(len(ls)):
    a = ls[i]
    count = 0
    for j in range(len(ls[i::])):
        if a < 0:
            if ls[j] > 0:
                break
            else:
                count += 1
        elif a == 0:
            count += 1
            a = ls[j+1]
        else:
            if ls[j] < 0:
                break
            else:
                count += 1


        if max_count < count:
            max_count = count

print(max_count+1)


