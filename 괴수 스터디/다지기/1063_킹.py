# 구현

# 8 x 8 고정이기때문에 그냥 한다.
# 딕셔너리 활용해서

# 입력된 값에 따라 이동좌표 불러와서 사용

king, stone, N = input().split()
N = int(N)

# 각 좌표 위치 확인하기,
# 영어가 열, 숫자 행
# 영어는 숫자로 변경

def find_position(position):
    # string 이니까 첫번째는 영어
    # 기준점을 가지고 찾아야함 열은 A 행은 
    x = ord(position[0]) - ord('A')
    y = 8 - int(position[1])
    return x,y

def final_position(x,y):
    x = chr(x + ord('A'))
    y = str(8 - y)
    return x + y


# 초기 좌표값 커멘드따라 더하고 뺄 수 있게 숫자로 변환
king_x, king_y = find_position(king)
stone_x,stone_y = find_position(stone) 

# 이동 좌표들 모은 dic
moving = {
    "R": (1,0), "L": (-1,0), "B": (0,1), "T": (0,-1), "RT": (1,-1), "LT": (-1,-1), "RB": (1,1), "LB": (-1,1) 
    }

for i in range(N):
    # 입력받기
    goto = input()
    dx, dy = moving[goto]
    # 입력에 따른 진행
    # 바뀐 좌표
    king_cx = king_x + dx
    king_cy = king_y + dy

    # 범위 내인가? 아니면 그냥 다음꺼
    if 0 <= king_cx < 8 and 0 <= king_cy < 8:
        # 범위 내에 움직인 좌표가 돌이랑 일치하나?
        if king_cx == stone_x and king_cy == stone_y:
            # 일치하면 돌 이동시켜바바
            stone_cx = stone_x + dx
            stone_cy = stone_y + dy
            if 0 <= stone_cx < 8 and 0 <= stone_cy < 8:
                stone_x  = stone_cx
                stone_y  = stone_cy
                king_x = king_cx
                king_y = king_cy
        else:
            king_x = king_cx
            king_y = king_cy
    else:
        pass

# 마지막 좌표 출력

print(final_position(king_x,king_y))
print(final_position(stone_x,stone_y))
