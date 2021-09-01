a = int(input())
ls = list(map(int, input().split()))

# from itertools import permutations
 
# # 주어진 값 입력
# n = int(input())
# a = list(map(int, input().split()))
 
# # permutation 저장(per: reference of permutation tuples)
# per = permutations(a)
# ans = 0

# for i in per:
#     siba = 0
#     for j in range(len(i)-1):
#         siba += abs(i[j]-i[j+1])
#     if siba > ans:
#         ans = siba
# print(ans)

ls.sort(reverse=True)

ps = []
lenth = len(ls)
# print(lenth)
if lenth%2 == 0:
    lenth = lenth//2
    for i in range(lenth):
        if i%2 == 0:
            ps.insert(len(ps),ls[i])
            ps.insert(0,ls[a-1-i])
        else:
            ps.insert(len(ps),ls[a-1-i])
            ps.insert(0,ls[i])
else:
    lenth =lenth//2 + 1
    # print(lenth)
    for i in range(lenth):
        if i%2 == 0:
            ps.insert(0,ls[-1])
            ps.insert(len(ps),ls[0])
        else:
            ps.insert(len(ps),ls[-1])
            ps.insert(0,ls[0])
        
        ls = ls[1:-1]
        print(ls)

# print(ls)
# if len(ls)%2 != 0:
#     if abs(ls[0]-ps[0]) > abs(ls[0]-ps[-1]):
#         ps.insert(0,ls[0])
#     else:
#         ps.insert(len(ps),ls[0])


print(ps)
# print(ps)
sum_si= 0

for j in range(len(ps)-1):
    sum_si += abs(ps[j]-ps[j+1])

print(sum_si)