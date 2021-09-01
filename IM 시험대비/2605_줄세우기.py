'''
줄 세우는 방법

첫번째
'''
'''

1 2 3 4 5

0 1 1 3 2
0
1

1
2 1

1
2 3 1 4 5

3




'''


N = int(input())

student = list(range(1,N+1))
# print(student)
number = list(map(int,input().split()))

ls = []

for i in range(N):
    ls.insert(i - number[i], student[i])

print(*ls)

print('hello word')
