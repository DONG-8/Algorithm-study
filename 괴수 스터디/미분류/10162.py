n = int(input())

def susu(T):
    a = 0
    b = 0
    c = 0 
    if T%10 != 0: 
        return -1
    
    while T!=0:
        if T >= 300:
            T -= 300
            a += 1
        elif T >= 60:
            T -= 60
            b +=1
        elif T >= 10:
            T -= 10
            c += 1
    return a,b,c

if susu(n) == -1:
    print(-1)
else:
    print(*susu(n))



# else:
#     if T >= 300:
#         T -= 300
#         a += 1
#     elif T >= 60:
#         T -= 60
#         b +=1
#     elif T >= 10:
#         T -= 10
#         c += 1
# 