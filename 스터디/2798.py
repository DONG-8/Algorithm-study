'''
블랙잭
카드의 합이 21을 넘지 않는 한도 내에서, 
카드의 합을 최대한 크게 만드는 게임이다. 

3장의 카드를 골라야 한다.
n  : 주어지는 카드 갯수
m : 주어지는수

3장으로 최대한 가까운 값을 구해야한다.

'''
'''
5 21
5 6 7 8 9
'''
# 21이 있냐?
'''
n, m = map(int, input().split())
num_ls = list(map(int,input().split()))
# 중복이 허용된 경우이다.
hubo = []
for i in range(1<<n):
    ls = []
    for j in range(n):
        if i & 1<<j:
            ls.append(num_ls[j])
    if len(ls) == 3:
        hubo.append(ls)

# print(hubo)
lenth = len(hubo)
big = sum(hubo[0])
final = []
for i in range(lenth):
    if sum(hubo[i]) <= m:
        final.append(sum(hubo[i]))

print(max(final))

또 시간초과;; 부분집합은 답이 없다.
'''

'''
그러면 그냥 순열을 이용
# import itertools

# n, m = map(int, input().split())
# num_ls = list(map(int,input().split()))
# # 중복이 허용된 경우이다.
# a =list(itertools.permutations(num_ls, 3))

# print(a)
'''

n, m = map(int, input().split())
num_ls = list(map(int,input().split()))

big0  = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sums = num_ls[i] + num_ls[j] + num_ls[k]
            if sums <= m and big0 < sums:
                big0 = sums

print(big0)







