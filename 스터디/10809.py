# s = input()

# alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# ls = []
# for j in range(len(alpa)):
#     ls.append(-1)
# count = 0
# for i in s:
#     if ls[alpa.index(i)] == -1:
#         ls[alpa.index(i)] = count
#         count += 1
#     elif ls[alpa.index(i)] != -1:
#         count += 1
#     else:
#         pass

# print(*ls)

s = input()     

alpa = 'abcdefghijklmnopqrstuvwxyz'

for i in alpa:
    print(s.find(i), end=' ')
