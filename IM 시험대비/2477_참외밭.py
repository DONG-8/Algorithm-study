'''

동 1 서 2 남 3 북 4

같은 방향 숫자가 2번 나오는 순간 그 전의 인덱스 값을 구한다.
이 각각 인덱스 값의 1번 인덱스의 곱은 빼야 할 넓이.

2개의 비어있는 인덱스 생성

값 대입
나머지 값은 어떻게 구하는가?

'''

import sys
sys.stdin = open('input.txt')

N = int(input())

idx_check = [0]*5
two_idx = []
# value_check = [[],[],[],[],[]] # 방향에 따른 값 체크
# 2개인 리스트만 나충에 추출
ls = []
for i in range(6):
    idx, value = map(int,input().split())
    idx_check[idx] += 1
    ls.append([idx, value])

for i in range(len(ls)):
    if ls[i][0] == 4 and ls[(i+1)%6] == 2:
        ls = ls[i:len(ls)+1] + ls[i]
print(ls)
# 4 다음엔 2
# 2 다음엔 3
# 3 다음엔 1
# 1 다음엔 4
number = [4,3,2,1]
num =  [4,2,3,1,4,2]
for i in range(len(ls)):
    if ls[i][0] != num[i]:
        minus = ls[i-1][1]*ls[i][1]*N
        number.remove(ls[i][0])
        number.remove(ls[i-1][0])
        break
# print(number)
# print(ls)
Area = N
for i in range(len(ls)):
    for j in number:
        if ls[i][0] == j:
            # print(ls[i][1])
            Area *= ls[i][1]
            # print(Area)

result = Area - minus
print(result)

# only_number = []
# for i in range(len(idx_check)):
#     if idx_check[i] == 1:
#         only_number.append(i)
# total_Area = 1
# for idx, value in ls:
#     for j in only_number:
#         if idx == j:
#             total_Area *= value
#
# print(total_Area)
#
# first = [1,2,3,4]
#
# first.remove(only_number[0])
# first.remove(only_number[1])
# print(first)
# first.sort()
# print(ls)
# if first == [1,3]:
#     for i in range(len(ls)):
#         print((i+1)%6)
#         if ls[i%6][0]== 1 and ls[(i+1)%6][0] == 3:
#             result = (total_Area - ls[i % 6][1]*ls[(i+1)%6][1])*N
# elif first == [2, 4]:
#     for i in range(len(ls)):
#         if ls[i%6][0]== 2 and ls[(i+1)%6][0] == 4:
#             result = (total_Area - ls[i % 6][1]*ls[(i+1)%6][1]) * N
#
# elif first == [1, 4]:
#     for i in range(len(ls)):
#         if ls[i%6][0]== 4 and ls[(i+1)%6][0] == 1:
#             result = (total_Area - ls[i % 6][1]*ls[(i+1)%6][1]) * N
# elif first == [2, 3]:
#     for i in range(len(ls)):
#         if ls[i%6][0]== 3 and ls[(i+1)%6][0] == 2:
#             result = (total_Area - ls[i % 6][1]*ls[(i+1)%6][1]) * N
#
# print(result)
#













# twoidx 의 처음  값을 인덱스로 하는 곳에서의 두번째 값
# twoidx 의 두번째 값을 인덱스로 하는 곳에서의 첫번째 값
# 을 곱해주면 빼야 할 넓이
# print(two_idx,value_check)
# minus_Area = value_check[two_idx[0]][1] * value_check[two_idx[1]][0] * N
#
# total_area = sum(value_check[two_idx[0]])*sum(value_check[two_idx[1]]) * N
#
# result = total_area - minus_Area
# print(result)

# 랜덤한 방향성 때문에 이 방법은 불가능함








