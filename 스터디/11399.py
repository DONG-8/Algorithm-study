T = int(input())

num_list = list(map(int, input().split()))

num_list.sort(reverse=True)
add = 0
for i in range(len(num_list)):
    add += sum(num_list[i:])

print(add)