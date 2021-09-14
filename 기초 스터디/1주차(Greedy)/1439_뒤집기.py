'''

0001100

111100011110001111

010 1번

1001

사이에 숫자가 있냐 없냐

'''

import sys
sys.stdin = open('test.txt')

num = input()

fnum = num
rnum = num
fnum = fnum.split('1')
rnum = rnum.split('0')

a = len(fnum)-fnum.count('')
b = len(rnum)-rnum.count('')

if a >= b:
    print(b)
else:
    print(a)
