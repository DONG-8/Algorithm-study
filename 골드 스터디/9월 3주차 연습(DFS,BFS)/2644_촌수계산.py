'''
1. dfs
2. bfs
'''

n = int(input())

start, end = map(int, input().split())

v = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

n2 = int(input())

for i in range(n2):
    temp1, temp2 = map(int, input().split())
    v[temp1].append(temp2)
    v[temp2].append(temp1)

'''
1. bfs

ans = -1

def dfs(n, cnt=0):
    global end, ans

    if n == end:
        ans = cnt

    for i in v[n]:
        if visited[i] == True:
            continue
        visited[i] = True
        dfs(i, cnt + 1)
        visited[i] = False

dfs(start, 0)
print(ans)

'''
ans = -1
que = []
que.append(start)
cnt = 0 
visited[start] = True
while len(que) != 0:
    size = len(que)

    # 여기가 새로운 que 갱신하는곳
    for _ in range(size):
        a = que.pop(0)
        # a = 7
        # 종료조건
        if a == end:
            ans = cnt

        # 이제 방문 안하고, 종료조건을 만족하지못한 
        for i in range(len(v[a])):
            if visited[v[a][i]]:
                continue

            visited[v[a][i]] = True
            que.append(v[a][i])
    cnt +=1
    

print(ans)









    
    



