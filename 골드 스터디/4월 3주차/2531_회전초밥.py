'''
회전초밥 벨트위에 음식 하나씩 올라간다.
초밥의 종류  === 번호
벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.
--> 같은 숫자가 여러번 나올 수 있다는 말임

행사 2개
임의의 한 위치로부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
초밥의 종류 하나가 쓰인 쿠폰을 발행하고 1번 행사에 참여 할 경우 
이 쿠폰에 적혀진 초밥 하나를 무료로 제공한다. 만양 이 번호에 적인 초밥이 현재 벨트 위에
없을 경우 요리사가 새로 만들어서 제공한다.


'''

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]

new_arr = arr + arr

sol = []
length = 0
dic = dict()
for i in range(n+k-1):
    slice_arr = new_arr[i:i+k]
    set_arr = set(slice_arr)
    # sol.append(slice_arr)
    if c not in slice_arr:
        count = (len(set_arr) + 1)
    else:
        count = (len(set_arr))
    
    if length < count:
        length = count

print(length)




# dic = dict()

# for i in range(1,k+1):
#     dic[i] = []

# for array in sol:
#     dic[len(set(array))].append(array)

# result = []

# for i in range(1,k+1):
#     if len(dic[i]) > 0:
#         result = dic[i]



# length = 0
# for k in result:
#     if c not in k:
#         xx = len(set(k)) +1
#     else:
#         xx = len(set(k))

#     if length < xx:
#         length = xx

print(length)