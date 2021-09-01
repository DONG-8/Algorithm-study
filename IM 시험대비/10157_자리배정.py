import sys
sys.stdin = open('input.txt')


C, R = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

if C*R < N:
    print(0)
else:
    visited = [[0]*R for _ in range(C)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = 0
    visited[x][y] = 1
    count = 1
    k = 0
    while count != N:
        cx = x + dx[k]
        cy = y + dy[k]
        if 0 <= cx < C and 0 <= cy < R and visited[cx][cy] == 0:
            visited[cx][cy] = 1
            count += 1
            x = cx
            y = cy
        else:
            k = (k+1)%4

    print('{} {}'.format(x+1,y+1))
