'''
N 덩어리로 잘라놓고 판매하고있다.

어떤 덩어리를 샀을 때에는 그 덩어리보다 싼 고기들은
얼마든지 덤으로 얻을 수 있다.

비용과 무게와의 관계가 서로 비례하는 관계가 아닐 수도 있다.

4 9
1 6
10 4
1 2
4 8

'''

import sys
sys.stdin = open('test.txt')

N, K = map(int, input().split())

meat = [list(map(int,input().split())) for i in range(N)]


meat.sort(key=lambda x: (x[1],-x[0]))
sumtot = 0
summoney = 0
result = 0
before_money = 0
count_same = 1
ls = []
for i in range(N):
    now_money = meat[i][1]
    if now_money == summoney:
        count_same += now_money
    else:
        count_same = now_money
        summoney = now_money

    sumtot += meat[i][0]
    if sumtot >= K:
        result = count_same
        ls.append(result)


onemoney = 0
for i in range(N):
    if meat[i][0] >= K:
        onemoney = meat[i][1]
        ls.append(summoney)
        break

print(ls)
if ls:
    print(min(ls))
else:
    print(-1)
