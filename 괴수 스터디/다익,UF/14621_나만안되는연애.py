# 크루스칼

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    # 최상위 부모 처리
    # 랭크 대신 사용
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
# 성별정보 받기
gender = list(input().split())

# find 사용을 위한 리스트
parent = [i for i in range(n + 1)]
pathsum = 0
pathnumber = 0

edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

# 가중치 작은것으로 정렬
edges.sort()

for edge in edges:
    # 쪼개기
    cost, a, b = edge
    #  성별 다른지 확인 부모요소가 다를때 합쳐주기
    if find(a) != find(b) and gender[a - 1] != gender[b - 1]:
        union(a, b)
        # 경로 값 추가
        pathsum += cost
        # 경로 확인용
        pathnumber += 1

if pathnumber == n-1:
    print(pathsum)
else:
    print(-1)