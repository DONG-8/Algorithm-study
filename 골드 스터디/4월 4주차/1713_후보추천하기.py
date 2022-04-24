n = int(input())

total_chu = int(input())

hu = list(map(int, input().split()))

# 알아야 하는 것

# 총 갯수 n

arr = [0]*(n) # n개의 액자가 들어 있는 칸
hubo = dict()


for i in range(total_chu):
    a = hu[i]   # 추천받는 사람의 번호
        # 길이가 넘어갈 때, 
    if a in hubo: 
        hubo[a][0] += 1
    else:
        if len(hubo) < n:
            hubo[a] = [1,i]
        else:
            # 딕셔너리 정렬 후 삭제 해야함
            # 투표순을 우선으로 정렬 후, 투표 수가 같다면, 먼저 들어 온 순서대로
            arr_to_del = sorted(hubo.items(), key=lambda x : (x[1][0], x[1][1]))
            del(hubo[arr_to_del[0][0]])
            hubo[a] = [1,i]

result = list(sorted(hubo.keys()))

for i in result:
    print(i, end=" ")


