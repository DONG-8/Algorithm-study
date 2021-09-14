
a = int(input())
b = int(input())
ls = []
for i in str(b)[-1::-1]:
    print(a*int(i))
    ls.append(a*int(i))

print(ls[2]*100 + ls[1]*10+ls[0])
