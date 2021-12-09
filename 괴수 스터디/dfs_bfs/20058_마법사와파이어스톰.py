'''
마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전할 수 있다.

N, Q가 주어지는데
이 N은 2^N X 2^N 의 격자를 형성한다.



'''


# L 에 따라 쪼개고 돌리는게 달라진다.
# ex) L --> 1 이면 2의 범위를 가지는데, 이는 분할정복을 통해 구할 수 있다.
# 회전 후에는 이 리스트를 탐색해서 0 이있는 곳의 정보를 확인한다.


# 녹은 지점의 값을 -1 해준다.

def melt_ice():
    for r,c in melting_point:
        if ice[r][c] == 0:
            continue
        ice[r][c] -= 1


# 원본에서 녹아야하는 얼음을 찾아준다.
# 0인 칸이 2개 이상이면 (상하좌우)
def find_melting_point(N):
    end = 2**N
    for r in range(end):
        for c in range(end):
            # 이 좌표에서 상하좌우 확인
            zero_check = 0
            for x,y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                # r,c 를 기준으로 이동한 좌표가 범위 내에 있을 때
                if 0 <= x <end and 0 <= y < end:
                    # 만약 이 좌표의 ice가 0 이라면 check
                    if ice[x][y] == 0:
                        zero_check += 1                            
            # 다 끝났을 때 zero_check >=2 면 리스트에 담기        
            if zero_check >= 2:
                melting_point.append([r,c])
    

# 회전이 끝난 후 원본을 변경시켜준다.
def copy_copy():
    for i in range(2**N):
        for j in range(2**N):
            ice[i][j] = copy_list[i][j]

# 회전을 위한 함수
# 각 영역에서 또 쪼개준다.
def rotate(x,y,num):
    # 좀 넘어가~~~
    # 나누게 되는 단위는?
    slice_num = num
    # 간격을 어디까지?
    end_of_list = 2**num
    # 분할된 부분의 모든 좌표 탐색
    for xx in range(x,x + end_of_list):
        for yy in range(y, y+ end_of_list):
            copy_list[yy][y+ end_of_list-1-xx] = ice[xx][yy]

    

# 분할을 위한 함수
def div(num):
    # num 에따라 2**num 만큼 분할
    # 이때는 분할의 기준점 좌표를 찾는것
    div_location_list = []
    for i in range(0,2**N,2**num):
        for j in range(0,2**N,2**num):
            # 좌표정보 넣기
            print(i,j,num)
            rotate(i,j,num)
    # num을 넘겨주는 이유는 여기서 내부 격자를 나누어주는 단위이자, range설정에 용이하다.
    
    
# input

N, Q = map(int,input().split())

ice = [list(map(int,input().split())) for _ in range(2**N)]

L_list = list(map(int,input().split()))

# --  input 완료

# 회전한 정보를 저장하기 위한 비어있는 리스트.

copy_list = [[0]*(2**N) for _ in range(2**N)]
print(copy_list)
for i in range(len(L_list)):
    num = L_list[i]
    div(num)
    copy_copy()
    # 녹은 지점 체크
    visit = [[0]*(2**N) for _ in range(2**N)]
    melting_point = []
    find_melting_point(N)
    melt_ice()

    # 회전 및 녹는 과정 종료

# 모든 과정이 끝났을 때,
# 1. 남아있는 얼음의 합 --> sum
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
#  --> 0이 아닌지점 visit == 0인 지점을 탐색할때마다 count += 1

#이러면 끝 나머지는 일어나서 한다.