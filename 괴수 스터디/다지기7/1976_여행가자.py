

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        return

N = int(input())
M = int(input())
parent = [0]*(N+1)

# 부모 세팅
for i in range(1,N+1):
    parent[i] = i

# 
for i in range(1,N+1):
    # i 번째 줄의 연결정보 받기
    arr =list( map(int, input().split()))
    # 연결정보중 연결된 것이 있는것을 확인하는 for문
    for j in range(1, len(arr)+1):
        # 연결되어있다면!
        if arr[j-1] == 1:
            union(parent,i,j)


loot = list(map(int, input().split()))

result = []

for i in loot:
    result.append(find(parent,i))

# 한 길로 연결되었는지 확인하기
# result 의 모든 부모가 같다면?!

a = result[0]
for i in range(1,len(result)):
    if a != result[i]:
        print("NO")
        break
else:
    print("YES")