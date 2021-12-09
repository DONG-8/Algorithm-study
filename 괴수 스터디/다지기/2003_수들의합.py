n, m = map(int, input().split())
sum_seed = list(map(int, input().split()))

# 투포
# 초기 스타트지점
left, right = 0, 1
# 카운팅용
cnt = 0
# 오른쪽이 범위를 초과하고, 왼쪽이 오른쪽보다 낮은수일때 혹은 같을때까지 반복
while right <= n and left <= right:

    # 할려고하는거
    # 합 구간 찾기
    hap = sum_seed[left:right]
    total = sum(hap)
    


    # 합을 구했죠?
    if total ==  m :
        # 카운트 1 늘려주고
        cnt += 1
        # 포인터 오른쪽 이동
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(cnt)
