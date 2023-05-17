T = int(input())    # 테케
for _ in range(T):
    N,M = map(int, input().split())     # 입력
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))
    # -----
    result = 0
    M_arr.sort()
    N_arr.sort()

    # N의 집합해서 M의 집합의 값보다 작은 값으로 이루어진 쌍의 갯수
    # 정렬하고, 중간 인덱스의 값이 내 값보다 작은 최대지점을 찾는다.
    for i in range(N):
        l,r = 0, M-1
        while l<= r:
            mid = (l+r) //2
            if M_arr[mid] >= N_arr[i]:
                r = mid - 1
            else:
                l = mid + 1
        result += l
    print(result)

        
