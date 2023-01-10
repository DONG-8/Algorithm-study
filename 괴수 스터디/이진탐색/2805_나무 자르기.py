
# N 이 매우매우 크네요
# 이분탐색 or 그리디 or 정수론

# 나무를 최대 높이로 했을 때 가져가기
# 높이값을 범위로 이분탐색

N,M = map(int, input().split())

arr = list(map(int, input().split()))

l,r = 1, max(arr)
sum_of_heigth = 0
while l<=r:
    get_tree = 0
    mid = (l+r)//2
    for i in arr:
        if i > mid:
            get_tree += i-mid
    
    if get_tree < M:
        r = mid - 1
    else:
        l = mid + 1

print(r)