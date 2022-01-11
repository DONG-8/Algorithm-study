M, N = map(int, input().split())

# 소수들이 들어갈 빈 리스트 생성

for i in range(M,N+1):

    flag = False
    if i == 1 :
        continue
    
    for k in range(2,i):
        if k*k > i:
            break
        
        if i % k == 0:
            flag = True
            break
    if flag == False:
        print(i)
