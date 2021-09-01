# 설탕배달

'''
3키로 봉지 5키로 봉지
정확하게 N 키로그램 배달해야함


'''
n = int(input())
ls = []
for i in range(n//3+1):
    for j in range(n//3+1):
        if 3*j+5*i == n:
            ls.append(i+j)

if ls == [] :
    print(-1)
else:
    print(min(ls))

'''
1946
1065
1541
'''

