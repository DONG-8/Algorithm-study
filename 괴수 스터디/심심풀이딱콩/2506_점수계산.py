N = int(input())

arr = [0]+list(map(int, input().split()))

result = [0]*(N+1)
for i in range(len(arr)):
    if arr[i] == 1:
        result[i] = result[i-1]+1
    else:
        result[i] = 0

print(sum(result))
