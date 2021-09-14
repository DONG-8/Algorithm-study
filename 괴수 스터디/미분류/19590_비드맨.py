'''

다른종류 구슬 2개면 뽀사짐
'''

# 최대 값 찾고
# 제일 작은 값 찾고 빼주고
# 다시 최대값 갱신하고

# 구슬의 종류

import sys
sys.stdin = open('test.txt')

n = int(input())

num = [int(input()) for _ in range(n)]

num.sort(reverse=True)
# print(num)
big_size = num[0]
# print(result)
other = sum(num[1:n])
# print(big_size, other)

while True:
    if other > big_size:
        if (other - big_size)% 2 == 1:
            print(1)
            break
        else:
            print(0)
            break

    else:
        result = big_size - other
        print(result)
        break










