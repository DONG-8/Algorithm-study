
N = int(input())

num_list = list(map(int, input().split()))
sum_of_gugan = 0
b = -1000
for i in range(N):
    now = num_list[i]
    sum_of_gugan += now

    sum_of_gugan = max(now, sum_of_gugan)
    b = max(sum_of_gugan, b)

print(b)
