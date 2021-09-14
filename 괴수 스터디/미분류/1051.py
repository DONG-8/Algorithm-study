# 숫자 정사각형

'''
n,m = 3,5

42101
22100
22101 >> 이게 직사각형

꼭지점에 쓰여있는 수가 
모두 같은 가장 큰 정사각형을 찾는 프로그램

'''
'''
3, 5 면 3행 5열
N M 중에서 작은수만큼이 최대로 생성될 수 있는 정사각형의
갯수이다.

큰거부터 내려가면서 탐색하는것이 효율적으로 보인다.

42101
22100
22101

'''

n, m = map(int, input().split())
ls = []
for i in range(n):
    ls.append(list(input()))

if n> m:
    a = m
else:
    a = n


lenth = []
for i in range(n): # 0,1,2
    for j in range(m): # 0,1,2,3,4
        for num in range(a-1,-1,-1): # 2,1,0 a=3
            if j+num > m-1 or i+num > n-1:
                continue
            
            if ls[i][j] == ls[i+num][j] == ls[i+num][j+num] == ls[i][j+num]:
                lenth.append(num+1)

# print(lenth)

Area = max(lenth)**2
print(Area)

