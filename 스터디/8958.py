n = int(input())
i = 1
ls = []
while i <= n:
    m = input()
    ls.append(m)
    i +=1
count = 0
summs = 0
for j in ls:
    for i in j:    
        if i == "O":
            count += 1
            summs += count
        if i == "X":
            count = 0
    print(summs)
    summs = 0
    count = 0
