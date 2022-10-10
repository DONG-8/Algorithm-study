# 2,3

# print(3, 2%3)
# # 32
# print(2, 3%2)
# # 2 1

# print(1, 2%1)
# print(0,0%1)

def GCD(a,b):
    while a%b != 0:
        a,b = b, a%b
    return b


dp = [0 for _ in range(1003)]
dp[1] = 3

# 0,2 1,2 2,2        

# 3
# 0,3 1,3 2,3 3,3

# 최대공약수가 1이 아니면, 나누었을때 더 작은 좌표가 존재한다는거임 
# ex) 2,4 -> 최대 공약수 -> 2 -> 1,2 -> 있쥬?

for i in range(2,1003):
    count = 0
    for j in range(1,i+1):
        a = GCD(i,j)
        if a == 1:
            count += 2
    dp[i] = dp[i-1] + count

#



T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])
    
    