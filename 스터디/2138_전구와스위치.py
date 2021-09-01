import sys

sys.stdin = open('test.txt')

N = int(input())

first = list(map(int, input()))
final = list(map(int, input()))

# 결국 처음만 결정되고 따라가게 하면 된다.

def switch(arr, on):
    count = 0
    if len(arr) == 1:
        if arr == final:
            return count
        else:
            count += 1
            return count

    if on == 1:
        arr = first[::]
        arr[0] += 1
        arr[0] %= 2
        arr[1] += 1
        arr[1] %= 2
        count += 1

    # print(first_on, first)
    for i in range(1, N - 1):
        if arr == final:
            break

        if arr[i - 1] == final[i - 1]:
            continue
        else:
            count += 1
            for mi in range(-1, 2):
                arr[i + mi] += 1
                arr[i + mi] %= 2

    if arr != final:
        arr[-1] += 1
        arr[-1] %= 2
        arr[-2] += 1
        arr[-2] %= 2
        count += 1

    if arr == final:
        return count
    else:
        return -1


a = switch(first, 1)
b = switch(first, 0)
if b != -1 or a != -1:
    if b != -1:
        print(b)
    elif a != -1:
        print(a)
else:
    print(-1)

# def switch(arr,on_off, idx):
#     global count
#
#     if arr == final:
#         print('일치합니다')
#         print(arr)
#         print()
#         return
#     if N == idx:
#         if arr == final:
#             print(arr,'일치합니다')
#             pass
#         else:
#             print(arr, '다 해도 안됩니다')
#
#     # for i in range(2):
#     #     switch(arr,i,idx+1)
#
#
#     if on_off == 1:
#         try:
#             for i in range(-1,2):
#                 arr[idx+i] += 1
#                 arr[idx+i] %= 2
#         except IndexError:
#             pass
#
#         switch(arr,1,idx+1)
#         switch(arr,0,idx+1)
#     else:
#         switch(arr, 1, idx + 1)
#         switch(arr, 0, idx + 1)
#
# idx = 0
# count = 0
#
# switch(first,1,idx)
# # switch(first,0,idx)
