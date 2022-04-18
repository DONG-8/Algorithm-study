n = int(input())
# in_Car = total_arr

# a b c d e
# b a d c e
# a랑 b 가 다르다 추월
# a가 나올때 까지는 체크 x
# c d 다르네? 그럼 다시 c 나올때 까지 체크
# 
join, end = dict(), []

for i in range(n):
    car = input()
    join[car] = i

for i in range(n):
    car = input()
    end.append(car)

# print(join)
count = 0

for i in range(n-1):
    for j in range(i+1,n):
        # 나오게 된 차량부터 순서대로 확인
        # 만약 나오게 된 차량의 들어갔을때의 인덱스 값보다 현재 차량 뒤에 나오는
        # 차량의 들어갈때 인덱스 번호보다 크다면 추웧 한 것이므로 제거해줌
        if join[end[i]] > join[end[j]]:
            count += 1
            # 이미 이 차가 추월했음을 확인했기 때문에 
            break

print(count)
            
        