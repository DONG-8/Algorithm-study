'''
이 문제에서 가장 중요한점
N 의 범위  : 1 <= N,M <= 1000000
100만단위 단순 in 으로 풀면 100% 시간초과난다. - by templates

'''
def two_point(num):    
    global result

    s = 0
    e = N - 1
    while s <= e:
        m = (s + e) // 2

        if note_1[m] == num:
            e = m
            result = 1
            return

        elif num > note_1[m]:
            s = m + 1
        else:
            e = m - 1
    
    return result
    
# 테스트 케이스의 수
T = int(input())
for i in range(T):
    # 수첩 1에 적어 놓은 정수의 개수
    N = int(input())

    # 여기는 물어본 숫자 list
    note_1 = list(map(int, input().split()))

    # 노트 2에 적은 정수의 갯수
    M = int(input())

    # 봤다고 주장한 숫자
    note_2 = list(map(int, input().split()))

    # 이진 탐색을 위한 정렬
    note_1.sort()
    for i in range(M):
        result = 0
        two_point(note_2[i])
        print(result)







