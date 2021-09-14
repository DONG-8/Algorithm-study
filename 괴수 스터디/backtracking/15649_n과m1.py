'''

n자리 m진수
'''

# 중복 상관 x
# 템플릿 2번 순열 같은 숫자라도 위치가 다르면 다른거
import sys

sys.stdin = open('test.txt')

m, n = map(int, input().split())
arr = [0] * n

visited = [False]*(m+1)

def recur(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(1,m+1):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = i
        recur(cur+1)
        visited[i] = False

recur(0)
