import pprint

N = int(input())

paper_list = [ list(map(int, input().split())) for _ in range(N)]

zero_count = 0
one_count = 0
minus_count = 0

# length = N//3 -> 탐색해야하는 길이

def division_list(N,length,arr):
    global zero_count, one_count, minus_count
    if not arr or N == 0:
        return
    
    if length == 0:
        length = 1

    count = 0
    arr_first_number = arr[0][0]
    for x in range(N):
        for y in range(N):
            if arr[x][y] == arr_first_number:
                count += 1
            else:
                break
    # 총 카운트가 맞다면?
    if count == N**2:
        if arr[0][0] == 1:
            one_count += 1
        elif arr[0][0] == 0:
            zero_count += 1
        elif arr[0][0] == -1:
            minus_count += 1
        
        return
    

    else:
        b = length//3
        for i in range(3):
            for k in range(3):
                ls = []
                for j in range(k*length,(k+1)*length):
                    a = arr[j][i*length:(i+1)*length]
                    ls.append(a)
                # print(ls)
                division_list(length,b,ls)
                # print('종료-----------')


division_list(N,N//3,paper_list)
print(minus_count)
print(zero_count)
print(one_count)
# print(zero_count,minus_count,zero_count)
'''
# 분할해보기

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

# length = 1
# N = 3
# for i in range(length):
#     # 0 1 2
#     a = arr[i:(i+1)*length][i:(i+1)*length]
#     print(a)

분할 성공
length = N//3
for i in range(length):
    for k in range(length):
        ls = []
        for j in range(k*length,(k+1)*length):
            a = paper_list[j][i*length:(i+1)*length]
            ls.append(a)
            print(ls)
        
'''
# N = 3
# arr = [[0, 1, -1], [0, 1, -1], [0, 1, -1]]

# length = 1

# for i in range(3):
#     for k in range(3):
#         ls = []
#         for j in range(k*length,(k+1)*length):
#             a = arr[j][i*length:(i+1)*length]
#             ls.append(a)

#         print(ls)
#         count = 0
#         # print(ls[0][0])
#         arr_first_number = ls[0][0]
#         # print(arr_first_number)
#         for x in range(length):
#             for y in range(length):
#                 print(x,y)
#                 if ls[x][y] == arr_first_number:
#                     count += 1
#         # # print(count)
#         print(ls)
#         # 총 카운트가 맞다면?
#         if count == length**2:
#             if ls[0][0] == 1:
#                 one_count += 1
#             elif ls[0][0] == 0:
#                 zero_count += 1
#             elif ls[0][0] == -1:
#                 minus_count += 1


현홍이 풀이

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
count = [0,0,0]
# [0,1,-1]
stack=[[0,0]]


def paper(y,x,N):
    check =True
    s = stack.pop()
    check = True
    num = graph[s[0]][s[1]]

    for i in range(s[0], s[0]+N):
        if check == False:
                break
        for j in range(s[1], s[1]+N):
            if graph[i][j] != num:
                check = False
                break

    if check ==True:
        count[num]+=1
    else:
        N = N //3
        for i in range(s[0],s[0]+N*3, N ):
            for j in range(s[1],s[1]+N*3, N ):
                stack.append([i,j])
                paper(i, j, N)

                # Q.append([i,j])

paper(0,0,N)

print(count[-1])
print(count[0])
print(count[1])





