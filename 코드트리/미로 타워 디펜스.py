# 1. 공격방향 상하좌우
# 2. 배열의 탐색 : 나선형
# 3. 연속 4번 이상 같은 몬스터가 있으면 제거
# 3-1. 만약 제거 하고 나서 또 연속하는 몬스터가 있다면 다시 제거 반복 없을때까지함
# 삭제가 일어나고 배열의 순서가 바뀐다.
# 같은 숫자끼리 짝을 지어준다. -> 갯수 + 숫자
# 그리고 재배열
# 격자 범위를 무시하면, -> 총 길이를 넘는 길이라면 슬라이싱
# 삭제되는 몬스터의 번호는 점수에 합쳐짐

# 입력 --
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
att = [list(map(int, input().split())) for __ in range(m)]

# -----

# 자주 쓰이는 변수들 지정

# 제거된 몬스터 점수의 합을 더해줄 변수

# attack x,y 오른 아래 왼 위


# ---
# 중심을 기준으로 배열을 배치 시키는 함수
# 재배치 -> 2차원 배열 반환
# 용도 1. 공격 이후 비어있는 배열을 제외하고 재배치 시킴
def rebatch(arr1d):
    if len(arr1d) <= n*n:
        arr1d = ([0]*(n*n) + arr1d + [0])[-(n*n):]
        # print('들어옴',arr1d,len(arr1d))
    else:
        arr1d = arr1d[-(n*n)+1:] + [0]
        # print('여기로옴')
        # print(arr1d,len(arr1d))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = 0,0
    visit= [[0]*n for _ in range(n)]
    visit[0][0] = 1
    arr[0][0] = arr1d[0]
    count = 0
    to = 0
    while [x,y] != center:
        nx = x + dx[to]
        ny = y + dy[to]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
            count += 1
            arr[nx][ny] = arr1d[count]
            x,y = nx, ny
            visit[x][y] = 1
        else:
            to = (to + 1)%4


# 공격 함수 input : 공격방향과 거리, output : 공격당한 좌표
# 좌표 기반으로 배열 변경
def attack(d,p,center):
    global result_answer
    ax = [0,1,0,-1]
    ay = [1,0,-1,0]
    for i in range(1,p+1):
        x = ax[d]*i + center[0]
        y = ay[d]*i + center[1]
        result_answer += arr[x][y]
        arr[x][y] = 0



# 배열 탐색 -> dx,dy 기반으로 탐색해서 1차원 list 반환
def arr_to_one(n):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = 0,0
    to = 0
    onearr = []
    if arr[0][0] != 0:
        onearr.append(arr[x][y])

    visit= [[0]*n for _ in range(n)]
    visit[0][0] = 1
    while [x,y] != center:
        nx = x + dx[to]
        ny = y + dy[to]
        # print(nx,ny,'nxny 입니다')
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
            if arr[nx][ny]:
                onearr.append(arr[nx][ny])
            x,y = nx, ny
            visit[x][y] = 1
        else:
            to = (to + 1)%4
            
    return onearr

# 연속하는 숫자가 있는지 탐색하는 함수 -> 제거
def find_continue_number(arr1d):
    global result_answer

    arr1d = arr1d + [-1]
    count = 1
    num = arr1d[0]
    s,e = 0,0
    answer = []
    for i in range(1,len(arr1d)):
        if arr1d[i] != num:
            if count < 4:
                for _ in range(count):
                    answer.append(num)
            else:
                result_answer += (num * count) 
            count = 1
            num = arr1d[i]
        else:
            count += 1

    return answer

# 같은 숫자끼리 짝지어주는 함수
def couple_number(arr1d):
    arr1d = arr1d + [-111]
    start = 0
    num = arr1d[0]
    count = 1
    answer = []
    for i in range(1,len(arr1d)):
        if arr1d[i] != num:
            answer.append(num)
            answer.append(count)
            num = arr1d[i]
            count = 1
        else:
            count += 1
    return answer


# attack(att[0][0],att[0][1],center,arr)
# a = arr_to_one(n)
# k = find_continue_number(a)
# kk = couple_number(k)
# xy = rebatch(kk)

center = [n//2, n//2]  # 홀수이기 때문에
result_answer = 0 
for d,p in att:
    # print(arr)
    attack(d,p,center)
    arr_one = arr_to_one(n)
    # print(arr)
    while True:
        new_one = find_continue_number(arr_one)
        if new_one == arr_one or new_one == []:
            arr_one =new_one[:]
            break
        arr_one = new_one[:]

    couple_one = couple_number(arr_one)
    rebatch(couple_one)
print(result_answer)