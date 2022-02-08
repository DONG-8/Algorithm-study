n = int(input())

ls =[]

i = 0
while True:
    if i == 0:
        ls.append(0)
    elif i == 1:
        if i == n:
            break
        else:
            ls.append(i)
    else:
        a = ls[i-1]+ls[i-2]
        if a >= n:
            break
        else:
            ls.append(a)
    
    i += 1

print(ls)

