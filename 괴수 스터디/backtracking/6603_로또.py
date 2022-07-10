#  순서가 상관이 있는 조합 만들기

def recur(cur, start):
    global n
    if cur == 6:
        print(*arr)
        return

    for i in range(start,len(lotto)):
        # if visit[i] == True:
        #     continue
    
        # visit[i] = True
        arr[cur] = lotto[i]
        recur(cur+1, i+1)
        # visit[i] = False

while True:
    arr_of_lotto = list(map(int, input().split()))

    # 종료조건
    if arr_of_lotto[0] == 0:
        break

    # 슬라이싱
    lotto = arr_of_lotto[1:]
    n = len(lotto)
    visit = [False]*len(lotto)
    arr = [0]*6
    recur(0,0)
    print()
    # 조합구하기
    
