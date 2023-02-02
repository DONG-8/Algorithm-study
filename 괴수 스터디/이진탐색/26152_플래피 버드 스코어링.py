# 단순 구현
# A,B의 길이가 25만이라서 2중 for문이 아니면 가능 해 보임
# 아니였음, 버드의 수에 따라 25만 * 25만 최대 62500000000
# 어쩌겠냐 줄일려면 이분탐색을 해야지 기준을 찾자! 
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bud = int(input())
bud_length = list(map(int, input().split()))

# 이분탐색
arr = []
for i in range(len(A)):
    arr.append(A[i] - B[i])

# 사이즈 필터 만들어주기
for j in range(1,len(arr)):
    if arr[j-1] < arr[j]:
        arr[j] = arr[j-1]
print(arr)
# 이분탐색


for length in bud_length:
    l,r = 0,len(arr)-1
    while l<=r:
        mid = (l+r)//2
        # print(mid,'미드')
        if arr[mid] < length:
            r = mid-1
        else:
            l = mid+1
    print(r+1)
