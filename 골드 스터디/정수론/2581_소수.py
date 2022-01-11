M = int(input())
N = int(input())

# 범위 내 소수찾기

result = 0
min_num = 0
first = False
for i in range(M,N+1):
    flag = False
    if i != 1:
        for k in range(2,i):
            if k*k > i:
                break

            if i%k == 0:
                flag = True

            if flag:
                break 
        
        if flag == False:
            if first == False:
                min_num = i
                first = True
            
            result += i

if min_num == 0:
    print(-1)
else:
    print(result)
    print(min_num)