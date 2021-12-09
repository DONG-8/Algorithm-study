'''
N번까지 신호등을 설치 해 두었다.


'''

n,k,b = map(int,input().split())

sinho = [1]*(n+1)

for i in range(b):
    num = int(input())
    sinho[num] = 0

guganhap = sum(sinho[1:k+1])


max_num = 0
for i in range(1,len(sinho)-k):
    guganhap = guganhap-sinho[i] + sinho[k+i]
    if max_num <= guganhap:
        max_num = guganhap


print(k-max_num)
