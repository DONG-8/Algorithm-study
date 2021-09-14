'''


'''

import sys
sys.stdin = open('test.txt')

N, M = map(int, input().split())

ls = list(map(int, input().split()))

ls.sort()

# 0 기준 양끝 두개 비교
# 더 큰값 은 마지막값

minus = []
plus = []
for i in range(N):
    if ls[i] < 0:
        minus.append(ls[i])
    elif ls[i] > 0:
        plus.append(ls[i])

plus.sort(reverse=True)

sum = 0
if minus == []:
    for i in range(0,len(plus),M):
        if i == 0:
            sum += plus[i]
            continue
        sum += 2*(plus[i])

elif plus == []:
    for i in range(0,len(minus),M):
        if i == 0:
            sum += abs(minus[i])
            continue
        sum += 2*(abs(minus[i]))

elif abs(minus[0]) > plus[0]:
    sum += abs(minus[0])
    for i in range(M,len(minus),M):
        sum += 2*(abs(minus[i]))

    for i in range(0,len(plus),M):
        sum += 2*(plus[i])

else:
    sum += plus[0]
    for i in range(M,len(plus),M):
        sum += 2*plus[i]

    for i in range(0,len(minus),M):
        sum += 2*(abs(minus[i]))

print(sum)
