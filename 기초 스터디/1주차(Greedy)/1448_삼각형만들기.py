'''

세 변의 길이의 최대 값 구하기

'''

import sys
sys.stdin = open('test.txt')

# 빨대의 갯수
N = int(input())

ls = []
for i in range(N):
    ls.append(int(input()))

ls.sort(reverse=True)

for i in range(N-2):
    if ls[i] < ls[i+1] + ls[i+2]:
        print(ls[i]+ls[i+1] + ls[i+2])
        break
else:
    print(-1)

