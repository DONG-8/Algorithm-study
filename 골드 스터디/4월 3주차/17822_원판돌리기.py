'''
원판 반지름 i
원판에는 m개의 정수가 적혀있다.
'''
from collections import deque
que = deque()

n, m, t = map(int, input().split())

arr = [deque(map(int, input().split())) for i in range(n)]

turn = [list(map(int, input().split())) for k in range(t)]

# d = 0 시계 d = 1 반시계
# 회전 시키기 함수
def rotate(x,d,k):
    for i in range(x-1,n,x): 
        if d == 0:
            arr[i].rotate(k)
        else:
            arr[i].rotate(-k)
        
def sum_of_circle():
    result = 0
    for i in range(n):
        result += sum(arr[i])
    
    return result

def find_same_number(num):
    zero_location = []
    # 인접하면서 같은 수 찾기
    # 인접한거만 찾게 하기
    # 같은 원의 경우
    for i in range(n):
        # 배열 안넘어가는 영역 찾기
        for j in range(m-1):
            if arr[i][j] != 0 and arr[i][j+1] != 0 and arr[i][j] == arr[i][j+1]:
                zero_location.append((i,j))
                zero_location.append((i,j+1))
        
        # 배열 맨끝과 처음이 같은지 찾기
        if arr[i][0] != 0 and arr[i][-1] != 0 and arr[i][0] == arr[i][-1]:
            zero_location.append((i,0))
            zero_location.append((i,m-1))

    # 외부 배열!
    # 같은 행에 대해서 확인해야함 행의 경우 m으로 체크
    for i in range(m):
        for k in range(n-1):
            if arr[k][i] != 0 and arr[k+1][i] != 0 and arr[k][i] == arr[k+1][i]:
                zero_location.append((k,i))
                zero_location.append((k+1,i))


    # 인접 한 수가 있어 zero list의 길이가 1 이상이라면 배열 0으로 세팅
    zero_location = list(set(zero_location))
# if len(zero_location) > 0:
#     # print(zero_location,'제로로케이션')
    for location in zero_location:
        # print(location, '로케이션')
        x,y = location
        arr[x][y] = 0        

    # 아니라면
    if len(zero_location) == 0:
        # 평균 구하기
        # print('평균구하기')
        zero_count = 0
        avg = 0
        # 평균을 구할 때, 0인 것이 들어있으면 0을 제외하고 평균을 구해줍니다/
        for i in range(n):
            avg += sum(arr[i])
            for j in range(m):
                if arr[i][j] == 0:
                    zero_count += 1
                
        
        avg_number = avg/ (n*m -zero_count)

        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0 and arr[i][j] > avg_number:
                    arr[i][j] -= 1
                elif arr[i][j] != 0 and arr[i][j] < avg_number:
                    arr[i][j] += 1

        

for tu in range(t):
    x,d,k = turn[tu]
    rotate(x,d,k)

    # 회전 이후
    # 수가 남아 있는 경우
    num = sum_of_circle()
    if num > 0:
        find_same_number(num)
    else:
        break

result = 0
for i in range(n):
    result += sum(arr[i])

print(result)
