import sys

N, M = map(int,sys.stdin.readline().split())

num_list =[0] + list(map(int, sys.stdin.readline().split()))

ls = [0]*(N+1)
ls[1] = num_list[1]
ls[2] = num_list[1] + num_list[2]

for i in range(N+1):
    if ls[i] == 0:
        ls[i] = ls[i-1]+ num_list[i]

# print(ls)

# print( N,M, num_list)
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    result = ls[e]-ls[s-1]
    print(result)
    
