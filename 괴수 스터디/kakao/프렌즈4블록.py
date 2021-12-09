'''
m 행
n 열
각 리스트의 원소 str로 이어짐
[
    "CCBDE", 
    "AAADE",
    "AAABF", 
    "CCBBF"
    ]

리스트와 다름이 없다.


'''


def solution(m, n, board):
    
    
    
    answer = 0
    return answer


#----------------------------------------------------
m = 4
n = 5
arr = [
    "CCBDE", 
    "AAADE",
    "AAABF", 
    "CCBBF"
    ]

# 만약 한줄에서 같은 문자가 2번이상 나온다면
# 다음줄에도 같은지 확인

# 숫자가 다른 경우도 있을 수 있으니 최소값으로 총 total에 더해준다
# 이미 방문한 장소면, 다음줄로 넘어간다 --> 방문배열 생성


# 4개짜리 찾기

# 기준점 기준 우하 대각

have_to_delet = []
def Find_block():
    dx = [0, 1, 1]
    dy = [1, 0, 1]

    # 삭제해야하는 기준 좌표 받아오기
    for i in range(m):
        for j in range(n):
            count  = 0
            x, y = i ,j
            name = arr[x][y]
            for k in range(3):
                cx = x + dx[k]
                cy = y + dy[k]

                if 0 <= cx < m and 0<= cy < n and name == arr[cx][cy]:
                    count += 1

            if count == 3:
                have_to_delet.append([x,y])

    return have_to_delet
print(Find_block())


def delete_block():

    dx = [0, 1, 1]
    dy = [1, 0, 1]

    for _ in range(len(have_to_delet)):
        x,y = have_to_delet.pop(0)
        arr[x][y] = 0
        for k in range(3):
            cx = x + dx[k]
            cy = y + dy[k]

            arr[cx][cy] = 0

print(arr)

    

    
    







