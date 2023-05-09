n = int(input())
ret = 0

for i in range(n):
    s = input()
    stk = []
    for a in s:
        if stk and stk[-1] == a:
            stk.pop()
        else:
            stk.append(a)
    if not stk:
        ret += 1

print(ret)