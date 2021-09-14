# 숫자 재배치

'''
두 정수 A와 B가 있을 때, A에 포함된 숫자의 순서를 섞어서
 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다. 

가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자.
 C는 0으로 시작하면 안 된다.

# 입력
1234 3456

# 출력
3421

'''
import itertools


A, B = map(int, input().split())
lenth = len(str(A))
# print(lenth)
A_num = []
for i in str(A):
    A_num.append(int(i))

random_A = list(itertools.permutations(A_num, lenth))
# print(random_A)

final_list = []
for i in random_A:
    num = ''
    for j in range(lenth):
        num += str(i[j])
    final_list.append(int(num))

small_than_B = []
for x in final_list:
    if len(str(x)) == lenth and x <= B:
        small_than_B.append(x)
    else:
        small_than_B.append(-1)

print(max(small_than_B))
    

