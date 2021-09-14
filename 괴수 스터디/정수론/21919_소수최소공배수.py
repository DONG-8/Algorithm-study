'''

소수판정
소수인경우 빈 리스트 추가

빈리스트 : -1 출력하고 종료
값이 있을경우 : 최소공배수 구하기
a,b = b,a%b

'''

import sys
sys.stdin = open('test.txt')


N = int(input())

num = list(map(int,input().split()))

# 소수판정
sosu = []

for i in range(N):
    if num[i] == 1:
        continue
    cnt = 0
    for j in range(2, num[i]):
        if j*j > num[i]:
            break

        if num[i] % j == 0:
            cnt +=1

    if cnt == 0:
        sosu.append(num[i])

if not sosu:
    print(-1)
    exit()
else:
    for i in range(len(sosu)-1):
        a, b = sosu[i],sosu[i+1]
        A,B = a, b
        while A%B != 0:
            A,B = B, A%B

        sosu[i+1] = (a*b//B)
print(sosu[-1])


