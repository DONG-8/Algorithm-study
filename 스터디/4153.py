# 직각삼각형
ls = []
while True:
    aaa =list(map(int, input().split()))
    if aaa == [0,0,0]:
        break
    ls.append(aaa)

for x in ls:
    x.sort()
    a = x[0]
    b = x[1]
    c = x[2]

    if (a**2)+(b**2) == c**2 :
        print('right')
    else:
        print('wrong')


# while True:
#     a, b, c = map(int, input().split())
#     if a == 0 and b ==0 and c ==0:
#         break
    

    
#     if (a**2)+(b**2) == c**2 :
#         print('right')
#     else:
#         print('wrong')


