'''
스크린칸은 N칸으로 나누어져 있다.
스크린의 아래쪽 M 칸을 차지하는 바구니가 있다.


'''

# 첫째 줄에 N과 M이 주어진다.

import sys
sys.stdin = open('test.txt')

N, M = map(int, input().split())

J = int(input())

num_x = [int(input()) for _ in range(J)]

# print(num_x)
start = 0
end = M
count = 0
for i in range(J):
    if start < num_x[i] <= end:
        continue
    else:
        if N >= num_x[i] > end:
            cha_e = num_x[i]-end
            start += cha_e
            end += cha_e
            count += cha_e
        elif 0 <= num_x[i] <= start:
            cha_2 = start - num_x[i] + 1
            start -= cha_2
            end -= cha_2
            count += cha_2

print(count)
