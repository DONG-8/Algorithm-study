word = input().split("-")
result = 0
num_arr = []
for wd in word:
    arr = wd.split("+")
    sum_arr = 0
    for num in arr:
        sum_arr += int(num)
    num_arr.append(sum_arr)

for i in range(len(num_arr)):
    if i == 0:
        result += num_arr[i]
    else:
        result -= num_arr[i]

print(result)
