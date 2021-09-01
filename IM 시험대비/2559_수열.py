
'''
입력
10 2
3 -2 -4 -9 0 3 7 13 8 -3

투포인터 : 조건을 한칸씩 밀어내기
이진탐색 : 조건을 가운데로
'''
import sys
sys.stdin = open('input.txt')


N, R = map(int, input().split())

temp = list(map(int, input().split()))
max_temp = sum(temp[:R])
result = max_temp
for i in range(N-R):
    max_temp = max_temp - temp[i] + temp[R+i]
    if max_temp > result:
        result = max_temp

print(result)



