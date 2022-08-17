def recur(key, start, arr, cur):
    global flag
    if start == key and cur != 0:
        flag = True
        # print(key, start, arr, cur, '들어옴')
        for i in arr:
            visit[keys.index(i)] = 1
        return

    if cur == N:
        return
    arr.append(dic[key])
    recur(dic[key], start, arr, cur + 1)


test_num = 1
while True:
    N = int(input())
    if N == 0:
        exit()

    dic = {}
    count = 0
    for i in range(N):
        a, b = input().split()
        dic[a] = b

    keys = []
    for key in dic.keys():
        keys.append(key)
    count = 0
    visit = [0]*N
    for key, value in dic.items():
        if visit[keys.index(key)] == 0:
            # 해당 key 값이 가진 value -> value의 각 key 값을 이용하여 이동
            print(key, value, '이거가지고 시작')
            flag = False
            recur(key, key, [key], 0)
            if flag == True:
                count += 1
    print(test_num, end=" ")
    print(count)
    test_num += 1


# keys = []
#     values = [[] for _ in range(N)]
#     i = 0
#     for key, value in dic.items():
#         keys.append(key)
#         values[i].append()

#  arr = list(range(N))
#     # print(arr)

#     for i in range(N):
#         for j in values[i]:
#             k = keys.index(j)
#             union(i, k)

#     print(test_num, end=" ")
#     print(len(set(arr)))


# def find(x):
#     if arr[x] == x:
#         return x
#     else:
#         arr[x] = find(arr[x])
#         return arr[x]


# def union(i, j):
#     x = find(i)
#     y = find(j)

#     if x > y:
#         arr[y] = arr[x]
#     else:
#         arr[x] = arr[y]
