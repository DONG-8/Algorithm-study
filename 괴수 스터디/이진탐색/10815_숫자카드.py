
# data input
N = int(input())
find_card = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

# 결과값을 보이기 위한 M 길이만큼의 배열
arr = [0]*M

# 탐색을 위한 정렬
find_card.sort()
# 완탐도 가능해보임

for i in range(M):
    result = 0
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end)//2

        if find_card[mid] == card[i]:
            result = 1
            break
        elif find_card[mid] > card[i]:
            end = mid - 1
        else:
            start = mid + 1
    
    arr[i] = result
    

print(*arr)