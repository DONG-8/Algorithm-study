import sys

sys.stdin = open('test.txt')

m, n = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

arr = [0]*n
visited = [False]*(m+1)

def recur(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(m):
        if visited[i]:
            continue
        visited[i] = True
        arr[cur] = num_list[i]
        recur(cur+1)
        visited[i] = False

recur(0)

