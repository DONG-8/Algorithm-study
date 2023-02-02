# 숫자 카드 N개 : 50만
# 정수 M : 50만

# 그냥 가져오면 되는거아님?

N = int(input())
Card = list(map(int, input().split()))
M = int(input())
Check = list(map(int, input().split()))
dic = {}
result = []
for i in range(N):
    a = dic.get(Card[i],0) + 1
    dic[Card[i]] = a

for j in range(M): 
    b = dic.get(Check[j],0)
    result.append(b)

print(*result)
