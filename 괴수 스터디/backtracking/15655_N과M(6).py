import sys
sys.stdin = open('test.txt')

m, n = map(int, input().split())

num_list = list(map(int,input().split()))
num_list.sort()

visited = [False]*m

# 순서 상관 없이 찾는것, 그러니 이미 쓰인것은 안쓰는것 ㄱ형 출력
arr = [0]*n
def recur(cur, start):
    if cur == n:
        print(*arr)
        return

    for i in range(start, m):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = num_list[i]
        recur(cur+1,i)
        visited[i] = False

recur(0,0)