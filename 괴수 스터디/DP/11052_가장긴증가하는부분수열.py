
N = int(input())
num_list = list(map(int,input().split()))

# 수열 크기 1 <=  <= 1000
# 수열의 값 , 1000까지

ls = [1]*N

for i in range(N):
    for j in range(i+1,N):
        if num_list[i] < num_list[j]:
            num_list[i] = num_list[j]
            ls[i] += 1

print(num_list)
print(ls)
print(max(ls))

