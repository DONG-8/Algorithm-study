# ACM 호텔

n = int(input())
ls = []
for i in range(n):
    a = list(map(int, input().split()))
    ls.append(a)


for a, b, c in ls:
    count = 0
    for i in range(1,b+1): # 같은층 호수
        for j in range(1,a+1): # 한층씩 증가
            count+=1
            if count == c:
                if i <10:
                    print(str(j)+"0"+str(i))
                else:
                    print(str(j)+str(i))


