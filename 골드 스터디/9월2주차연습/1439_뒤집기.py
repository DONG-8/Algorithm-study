num = input()

fnum = num
rnum = num
fnum = fnum.split('1')
rnum = rnum.split('0')
print(fnum,rnum)

a = len(fnum)-fnum.count('')
b = len(rnum)-rnum.count('')
print(a,b)
if a >= b:
    print(b)
else:
    print(a)
