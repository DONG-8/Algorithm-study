def solution(a):
    answer = 2
    # 결국 좌우 비교를해서, 나보다 작은값이 2개면 실패임 그렇기때문에 시작점과 끝점은 언제나 가능함
    left_min = [0] * len(a)
    right_min = [0] * len(a)
    left_min[0], right_min[-1] = a[0], a[-1]
    # left 에서 내 인덱스 이전에 가지는 가장 작은값 저장하기,
    for i in range(1,len(a)):
        if left_min[i-1] > a[i]:
            left_min[i] = a[i]
        else:
            left_min[i] = left_min[i-1]

    for i in range(len(a)-2,-1,-1):
        if right_min[i+1] > a[i]:
            right_min[i] = a[i]
        else:
            right_min[i] = right_min[i+1]

    for i in range(1,len(a)-1):
        l,r = left_min[i-1],right_min[i+1]
        if l < a[i] and r < a[i]:
            continue
        else:
            answer += 1
    return answer