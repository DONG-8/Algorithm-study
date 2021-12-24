'''


'''
# 0 의 자리에 들어갈 수 있는 숫자 탐색!

def into_zero_list(x,y):
    
    number = [1,2,3,4,5,6,7,8,9]

    for i in range(9):
        # 행검사
        if sdoku[x][i] in number:
            number.remove(sdoku[x][i])
        # 열검사
        if sdoku[i][y] in number:
            number.remove(sdoku[i][y])
        
    # 3x3 소속된곳 검사
    # 4행이면 3 4 5
    # 1행이면 0 1 2
    # 8행이면 6 7 8
    # 몫으로 범위지정
    x = x//3
    y = y//3
    for j in range(x*3,(x+1)*3):
        for k in range(y*3,(y+1)*3):
            if sdoku[j][k] in number:
                number.remove(sdoku[j][k])
    
    return number

# 하나의 자리에 대한 탐색을 모든 0에 대해서 진행한다.
def recur(x):
    #종료조건 2개
    global esc
    # 하나 완성된다면 종료
    if esc:
        return

    # 좌표의 끝을 지났으면 x = 0~8까지가면 모든 0을 다채움
    if x == len_zero_location:
        esc =True
        for nn in sdoku:
            print(*nn)
        return

    else:
        # x번째의 좌표 받기
        i,j = zero_location[x]
        # 들어갈 수 있는 숫자 리스트 받기
        arr = into_zero_list(i,j)
        # 만약 arr가 존재하지 않는다면 재귀를 실행못함
        for n in arr:
            sdoku[i][j] = n
            recur(x+1)
            sdoku[i][j] = 0


sdoku = [list(map(int, input().split())) for _ in range(9)]

# 0 인것들에만 값을 넣으면 되기 때문에 0부터 찾기

zero_location = []

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero_location.append([i,j])

len_zero_location = len(zero_location)


esc = False
recur(0)


