'''
세탁소 사장 동혁
거스름돈을 잘못 주는 리암

달러단위
쿼터 : 0.25 다임 0.10 니켈 0.05 페니 0.01

센트 단위
쿼터 25 다임 10 니켈 5 페니 1
'''

n = int(input())

for _ in range(n):
    T = int(input())
    # print(T)
    q = d = n = f = 0
    while T != 0:
        if T >= 25:
            T -= 25
            q += 1
        elif T >= 10:
            T -= 10
            d += 1
        elif T >= 5:
            T -= 5
            n += 1
        else:
            f += 1
            T -= 1
    print(q, d, n, f)


