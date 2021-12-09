# union find set

# ---------- 입력 -------------
# 첫줄에 n : 집합의 수 -- n+1
# 노드를 나타낼 집합 생성
def set(n):
    ziphap = list(range(n+1))
    return ziphap

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1

n, m = map(int, input().split())

par = set(n)
rank = [ 0 for _ in range(n+1)]
for i in range(m):
    mode, a, b = map(int,input().split())

    if mode == 0:
        union(a,b)
        # print(a,b, '유니온 하였습니다')
        # print('a의 결과', find(a), 'b의 결과', find(b))
    else:
        

        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    
