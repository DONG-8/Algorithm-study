'''

정렬부터 시키고

7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''

import sys
sys.stdin = open('input.txt')


N = int(input())

xy_list = [list(map(int, input().split())) for n in range(N)]

xy_list.sort()

# print(xy_list)

# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

# 최대 높이 이전과 이후로 나뉜다.

# 최대 높이를 구하기 위한 for문

y_max = 0
x_max = 0
idx_max = 0
for idx,max_num in enumerate(xy_list):
    if max_num[1] > y_max:
        y_max = max_num[1]
        x_max = max_num[0]
        idx_max = idx

# print(idx_max, x_max, y_max)

# 최대 값 까지 도달 이후에는
# 높이가 작아지기만 해야 한다.

# 최대 값 도달 이전까지는
# 높이가 증가하는경우만 생각 해야 한다.

Area = 0
height = xy_list[0][1]
wide = xy_list[0][0]

for i in range(len(xy_list)):
    if i <= idx_max:
    # 증가부분이라면
        if height <= xy_list[i][1]:
            if i == idx_max:
                Area += (xy_list[i][0] - wide) * height
                Area += xy_list[i][1]
                height = 0
                wide = xy_list[i][0]
            else:
                Area += (xy_list[i][0] - wide) * height
                height = xy_list[i][1]
                wide = xy_list[i][0]
                # 최댓값이라면

    # 최댓값 이후라면?
    # 제일 큰 값, 그다음 큰값 순으로 나가야 오류를 방지할 수 있다.
    elif i > idx_max:
        hubang = xy_list[i:N]
        hu_y_max = 0
        for idx, max_num in enumerate(hubang):
            if max_num[1] > hu_y_max:
                hu_y_max = max_num[1]

        if hu_y_max == xy_list[i][1]:
            Area += hu_y_max*(xy_list[i][0]-wide)
            wide = xy_list[i][0]

print(Area)



# if height <= xy_list[i][1]:
        #     height = xy_list[i][1]
        #     if i == N - 1:
        #         Area += height * (xy_list[i][0] - wide)
        # elif height > xy_list[i][1]:
        #     Area += height*(xy_list[i-1][0]-wide)
        #     wide = xy_list[i-1][0]
        #     height = 0
        #     if i == N-1:
        #         Area += xy_list[i][1]*(xy_list[i][0]-wide)




# print('final Area = {}'.format(Area))


