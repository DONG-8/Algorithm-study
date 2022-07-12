## 크루스칼 알고리즘

N = int(input())

M = int(input())

arr = []

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x,y):
    x = find(x)
    y = find(y)

    par[x] = y



for i in range(M):
    arr.append(list(map(int, input().split())))

## arr의 2번 index를 기준으로 오름차순 정렬
arr.sort(key=lambda x: x[2])

answer = 0

par = list(range(N+1))

for i in range(M):
    if find(arr[i][0]) == find(arr[i][1]):
        continue

    union(arr[i][0], arr[i][1])
    answer += arr[i][2]

print(answer)