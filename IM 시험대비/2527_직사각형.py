import sys
sys.stdin = open('input.txt')

for t in range(6):
    # xy_num = list(map(int, input().split()))
    #
    # print(xy_num)
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input().split())

    # print(x1, y1, x2, y2, x3, y3, x4, y4)

    a = [x1, y1, x2, y2]
    b = [x3, y3, x4, y4]
    # print(a,b)

    if a[0] > b[0]:
        x1, y1, x2, y2 = b
        x3, y3, x4, y4 = a

    # print(x1, y1, x2, y2, x3, y3, x4, y4)

    # 정리 끝
    if x2 < x3 and y2 < y3 or y4 < y1:
        # print(t, '만날 수 없음')
        print('d')
    if x2 == x3:
        if y2 == y3 or y1 == y4:
            print('c')
        if y3 < y2 or y4 > y1:
            print('b')
    elif x3 < x2 <= x4:
        if y2 == y3 or y1 == y4:
            print('b')
        if y3 < y2 or y4 > y1:
            print('b')