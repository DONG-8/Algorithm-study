import itertools

N = int(input())

num_list = list(map(int,input().split()))

plmi = list(input().split())
# print(num_list)
# print(plmi)


# 부호변경
buho = ['+','-','*','/']
buho_list = []
for i in range(len(plmi)):
    for j in range(int(plmi[i])):
        buho_list.append(buho[i])
# print(len(buho_list))
# 순열 만들기
result = set(itertools.permutations(buho_list, len(buho_list)))
result = list(result)
# print(result[1][0])

# print(result)
max_num = -1000000000
min_num = 1000000000

# 이 연산리스트를 순회할거임
for case in result:
    # 연산자를 받아옴
    total = num_list[0]
    for i in range(1,N):
        if case[i-1] == '+':
            total +=num_list[i] 

        if case[i-1] == '-':
            total -=num_list[i]
        if case[i-1] == '*':
            total *=num_list[i]
        if case[i-1] == '/':
            total /= num_list[i]
            total = int(total)

    if total > max_num:
        max_num = total

    if total < min_num:
        min_num = total 
    
print(max_num)
print(min_num)
    





