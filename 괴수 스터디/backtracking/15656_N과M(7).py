import sys
sys.stdin = open('test.txt')

m, n = map(int, input().split())

num_list = list(map(int,input().split()))
num_list.sort()

arr = [0]*n
# 같은숫자 출력되어도 상관이 없음
def recur(cur,start):
    if cur == n:
        print(*arr)
        return

    for i in range(start, m):
        arr[cur] = num_list[i]
        recur(cur+1,i)

recur(0,0)