# 소수 찾기

# 소수의 특징
# 나누었을때 본인말고 못나눔

#10 > 2 5, 8 2 4, 9 3 3 , 7 123456 101 
n = int(input())
a = list(map(int, input().split()))

#소수의 특징
# 1제외 본인 제외 범위나누었을때
# 2,34,5,6
# 하나라도 나누어떨어지면 소수 x
answer = 0
for i in a:
    if i== 1: 
        continue
    for j in range(2, i):
        if i % j == 0: #나누어떨어짐
            break 
    else:
        answer += 1

print(answer)

