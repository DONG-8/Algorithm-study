'''
아이디어

1. z모양 탐색(dfs) + 분할탐색(재귀)
2. 시간제한 0.5초  -- > 가지치기를 통한 모든경우 탐색 X

# 분할 조건
N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 
재귀적으로 순서대로 방문한다.
N = 1일때 까지 재귀적으로 방문


# 종료조건 : 원하는 좌표값일때

# 이동방법
기준점 기준
    우 아래 끝
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

'''

N, r, c = map(int, input().split())

count = 0
stop = 0
# 재귀 방문

def Z(x,y,N):
    global count, stop

    if stop == 1:
        print(count-1)
        exit()
    # N이 1이 되었을 때 탐색을 시작
    # 여기서 원하는 좌표를 만나면 종료
    if N == 1:
        dx = [0, 0, 1, 1]
        dy = [0, 1, 0, 1]
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            count += 1
            if cx == r and cy == c:
                stop = 1
                break
        return

    for i in range(x,x+2**N,2**(N-1)):
        for j in range(y,y+2**N,2**(N-1)):
            if i <= r < i + 2**(N-1) and j <= c < j+2**(N-1):
                Z(i, j, N - 1)

                if stop == 1:
                    print(count - 1)
                    exit()
            else:
                count += (2**(N-1))**2
                # print('실행되었습니다')



    # 아닐경우 재귀 분할

# 비어있는 좌표,
Z(0,0,N)
print(count-1)