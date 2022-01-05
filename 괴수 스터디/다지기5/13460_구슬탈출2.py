
# 빨파 좌표찾기 함수
# 2중 for문을 통한 단순탐색
def find_RB():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                arr[i][j] == '.'
                red = [i,j]
            if arr[i][j] == "B":
                arr[i][j] == '.'
                blue = [i,j]
            
            if red and blue:
                return [red,blue]

# 입력

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]


# 주의할 점 한쪽으로 길이 뚫려 있으면 쭉 간다! --> while문 사용
# 공은 동시에 움직임 --> 같은 반복문 안에서 작동
# 동시에 빠져도 실패! --> 조건
# 기울이는 동작그만 --> 더이상 못움직일때 --> list에 이동할 좌표가 없을 때

# 이동 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit