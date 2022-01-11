N = int(input())

x = N
for i in range(2, N+1):
    if i * i > N:
        break

    while x % i == 0:
        print(i)
        x //= i

if x!= 1:
    print(x)
if x == N:
    pass