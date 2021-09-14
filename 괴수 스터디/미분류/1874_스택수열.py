'''

후입선출구조

스택에 push 하는 순서는 받느딧 오름차순을 지키도록한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지 , 있다면 어떤 순서로 push와 pop연산을
수행해야 하는지 알아낼 수 있다.
'''

import sys
sys.stdin = open('test.txt')

N = int(input()) # 8

num_list = []
for n in range(N):
    num_list.append(int(input()))

# 만들고 싶은 순서
# [4, 3, 6, 8, 7, 5, 2, 1]
# print(num_list)

# 1 2 5 3 4
# 1 2 3 4 5 6 7 8 9

# 스택용 리스트
stack =[]
i = 1
num = 1
result = []
while i <= N*2:
    if not stack:
        stack.append(num)
        result.append('+')
        i += 1
        num += 1
    else:
        if stack[-1] == num_list[0]:
            stack.pop()
            num_list.pop(0)
            result.append('-')
            i += 1
        else:
            if num <= N:
                stack.append(num)
                result.append('+')
                i += 1
                num += 1
            else:
                result = ['NO']
                break

for i in range(len(result)):
    print(result[i])




'''

import sys
input = sys.stdin.readline
 
n = int(input())
targets = [int(input()) for _ in range(n)]
current = 1
stack, answer = [], []
 
for target in targets:
    while current <= target:
        stack.append(current)
        answer.append('+')
        current += 1
 
    if stack[-1] == target:
        answer.append('-')
        stack.pop()
 
if not stack:
    print('\n'.join(answer))
else:
    print('NO')


'''

















# stack = []
# i = 0
# num = 1
# plus_count = 0
# minus_count = 0
# result = []
# while num <= N:
#     stack.append(num)
#     plus_count += 1
#     result.append('+')
#     if num_list[i] == stack[-1]:
#         stack.pop()
#         minus_count += 1
#         result.append('-')
#         i += 1
#     num += 1
#
# print(result)
#
# if stack:
#     for i in range(len(stack)):
#         if num_list[i] == stack[-1]:
#             stack.pop()
#             minus_count += 1
#             result.append('-')
#             minus_count += 1
#         else:
#             result = 'no'
#             break
#
#
# if minus_count != N-1 or plus_count != N-1:
#     result = 'no'
# else:
#     for i in result:
#         print(i)



# 8까지의 숫자가 반복해서 들어가고

# 들어간 값이 수열의 값과 일치하면 po

# 일치하지 않다면 append

# 다 더해서 끝이 되었다면?

