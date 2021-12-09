'''
1 : 1개
2 : 3개
3 : 5개
4 : 11개
'''
import sys
ls =[0]*1001

ls[1] = 1
ls[2] = 3
for i in range(3,1001):
    if ls[i] ==0:
        ls[i]=ls[i-2]*2 + ls[i-1]

N = int(sys.stdin.readline())
print(ls[N]%10007)