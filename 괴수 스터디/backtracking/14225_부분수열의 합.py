N = int(input())
arr = list(map(int, input().split()))
combi = [0] * 2000001
def recur(start,num,cur,end):
    if end == cur:
        combi[num] = 1
        return
    
    for i in range(start,len(arr)):
        num += arr[i]
        recur(i+1,num,cur+1,end)
        num -= arr[i]

for n in range(1,N+1):
    recur(0,0,0,n)

for i in range(1,len(combi)):
    if combi[i] == 0:
        print(i)
        break
