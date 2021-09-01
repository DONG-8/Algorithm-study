

a, b = map(int,input().split())

num1 = (-a) + abs(((abs(a**2)+(-1*b)))**(0.5))
num2 = (-a) - abs(((abs(a**2)+(-1*b)))**(0.5))
s = int(num1)
x = int(num2)

if s > x:
    print(x, s)
elif s < x:
    print(s, x)
elif x == s:
    print(x)
else:
    pass

