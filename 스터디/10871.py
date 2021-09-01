# x보다 작은수

N, X = map(int, input().split())
ls = list(map(int, input().split()))
final = []
for i in ls:
    if X > i:
        final.append(i)

for i in final:
    print(i, end=" ")


