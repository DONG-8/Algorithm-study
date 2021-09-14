## 더하기 사이클
def sumend(n):
    if 0 < int(n) < 10:
        sum1 = ""
        n = "0" + n
        sum1 = n
        return sum1
    
    sum1 = 0
    for i in n:
        sum1 = sum1 + int(i)
    sum1 = str(sum1)
    return sum1


n = input()
count = 0
b = n
while True:
    if b=='0':
        print(1)
        break

    a = b[-1] + sumend(b)[-1]
    if int(a)  == int(n):
        count +=1
        print(count)
        break
    else:
        b = a
    count += 1
