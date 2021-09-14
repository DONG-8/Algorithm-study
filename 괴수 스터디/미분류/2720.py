'''
거스름돈
큰거부터 차례로 마이너스

500 100 50 10 5 1

'''

n = 1000- int(input())
a = 0
while n != 0:
    if n >= 500:
        n -= 500
        a += 1
    elif n >= 100:
        n -= 100
        a += 1
    elif n >= 50:
        n -= 50
        a += 1
    elif n >= 10:
        a += 1
        n -= 10
    elif n >= 5:
        n -= 5
        a += 1
    else:
        n -= 1
        a += 1
print(a)
        