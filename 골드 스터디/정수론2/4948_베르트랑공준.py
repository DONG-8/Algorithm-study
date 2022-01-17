
while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    for i in range(N+1,2*N+1):
        if i == 1:
            continue
        flag = True
        for k in range(2,i): 
            if k*k > i:
                break
            # 소수라면
            if i % k == 0: 
                flag = False
                break
        if flag:
            count += 1 
    print(count)
