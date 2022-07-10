N, K = map(int, input().split())

# K번째로 지우는 수를 구하시오
visit = [True]*(N+1)
visit[1] = False

count = 0
for i in range(2, N+1):
    if not visit[i]:
        continue
    for j in range(i, N+1, i):
        if visit[j] == False:
            continue
        else:
            count += 1
            visit[j] = False
            if count == K:
                print(j)
                exit()
        
    