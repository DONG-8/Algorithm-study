# union find 문제
'''

n개의 국가가 존재한다.
각 국가는 1부터 n까지의 번호를 가지고 있다.
또한, 모든 국가는 각자 자신의 국가의 힘을 상징하는 병력을 가지고 있다.

랭크 값에 따라 달라진다.

병력이 더 많은 나라가 승리하며 패배한 나라는 속국
남은 병력은 승리한 나라의 병력에서 패배한 나라의 병력 수치

'''

# union find 정의
def find(x):
    if num[x] != x:
        num[x] = find(num[x])
    return num[x]

# 1일때 병합
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        # 1 2 합쳤을때 큰쪽을 작은쪽으로 합치고
        num[b] = a
        power[a] += power[b]
    else:
        # 반대로 진행
        num[a] = b
        power[b] += power[a]

# 2일때 한다이
def union2(a,b):
    a = find(a)
    b = find(b)
    # 싸워서 이긴다면? 병력으로
    if power[a] > power[b]:
        # 병력차만큼 갱신
        power[a] -= power[b]
        # 그리고 하나로 병합
        num[b] = a
    # 병력이 같다면 둘다 멸망
    elif power[a] == power[b]:
        num[a] = 0
        num[b] = 0
    else:
        power[b] -= power[a]
        num[a] = b


# 입력받기

n, m = map(int, input().split())
power = [0]
num = [0]

for k in range(1,n+1):
    num.append(k)

for i in range(n):
    power.append(int(input()))

for j in range(m):
    O,P,Q = map(int, input().split())
    # print(O,P,Q)
    # 입력 후 union find 실행
    if O == 1:
        union(P,Q)
    else:
        union2(P,Q)

# 모든 과정이 거치고 나면
# -1로 멸망 혹은 본인들의 뿌리를 찾게 된다
# 그러면 남은 나라의 파워만 확인해주면 끝
print(num)
# 각 최상 머리 찾기

ls = []
for n in range(1,len(num)):
    parent = find(n)
    if parent not in ls and parent != 0:
        ls.append(parent)

print(len(ls))

power_sort = []
for i in range(len(ls)):
    power_sort.append(power[ls[i]])

power_sort.sort()

for k in power_sort:
    print(k, end=" ")

