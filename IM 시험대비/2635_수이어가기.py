'''

다음과 같안 규칙에 따라 수를 만들려고 한다.

'''
'''
양의 정수가 주어진다.

100 99 1 98 

'''

N = int(input())

ls = [N]
count = 0
for i in range(N):
    j = 1
    ls = [N]
    num = N - i
    ls.append(num)
    while True:
        num = ls[j-1] - ls[j]
        if num < 0:
            break
        ls.append(num)
        j += 1
    if count < len(ls):
        result = ls
        count = len(ls)



print(count)
print(*result)









