def get_distance(three):
    distance = 0
    A = three[0]
    B = three[1]
    C = three[2]
    for i in range(4):
        if A[i] != B[i]:
            distance += 1
        if A[i] != C[i]:
            distance += 1
        if B[i] != C[i]:
            distance += 1
    
    return distance

def recur(start,n):
    global min_distance
    if n == 3:
        result = get_distance(three)
        if result < min_distance:
            min_distance = result
        return

    for i in range(start,N):
        three.append(arr[i])
        recur(i+1, n+1)
        three.pop()

T = int(input())

for i in range(T):

    N = int(input())

    arr = list(input().split())
    # 같은 유형이 무조건 3명이 존재하게되는 경우의 명수#
    # 비둘기 집의 원리
    if N > 32:
        print(0)
    else:
        # 거리를 재는 원칙
        # 3명씩 자르고, 최소거리니까 최소값 지정해야
        min_distance = 10000000000000000
        # 배열에서 중복없이 3명씩 뽑기.
        three = []
        recur(0,0)
        print(min_distance)

