n = int(input())
ls = []

for i in range(1, n + 1):
    if i * i > n:    #모든 약수는 쌍으로 존재하는데, 
        break        #작은 쪽이 항상 루트 보다 작거나 같으니 작은 쪽만 모두 본다.

    if n % i == 0:
        ls.append(i)
        if i * i != n:
            ls.append(n // i)

ls.sort()

count = 0
for i in ls:
    if count % 10 == 0:
        print()
    print(i, end=" ")
    count +=1
