'''
1번부터 N번까지 N개의 풍선이 원형
i번 풍선 오른쪽  i+1, 왼쪽 i-1

1번 풍선은 왼쪽에 N번 N번 오른쪽은 1번 풍선이 있다.

종이 안에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.

규칙

1번부터 터트리기
풍선안에 종이에 적힌 수 만큼 이동, 다음 풍선, 양수일때는 오른쪽
음수일때는 왼쪽으로 이동
--> 이동할때는 이미 터진 풍선은 빼고 이동한다. 없애주어야 한다.


'''
# print(-1%3)
N = int(input())

arr = list(map(int, input().split()))
idx = list(range(2,1+N))

result = [1]
spot = 0
addnum = arr.pop(spot)


while len(arr) > 0:
    
    if addnum > 0:
        spot = (spot + (addnum-1))% len(arr)
    else:
        spot = (spot + (addnum))% len(arr)
    
    result.append(idx.pop(spot))
    addnum = arr.pop(spot)

print(*result)  

