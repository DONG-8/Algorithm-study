'''

민식이는 수학학원에서 단어수학 문제늘 푸는 숙제를 받았다.

N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져있다.

각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제

GCF + ACDEB 일때 A=9 B=4 D=6 E=5 F=3 G=7로 하면
두수합은 99437로 최대가 될것이다.

N 개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

'''

# 입력받기

# test-case
# 2
# GCF
# ACDEB
N = int(input())

# arr = [list(input()) for _ in range(N)]

arr = [[] for _ in range(8)]        # 리스트 입력, 각 자리별 알파벳 입력하면됨 수의 최대길이 8자리
alpa = dict()   #중복된 알파벳이 나오는지 확인하기위함

max_length = 0
for _ in range(N):
    a = input()
    length = len(a)
    max_length =max(length,max_length)
    for i in a:
        # 각 자리수에 맞게 입력
        arr[length-1].append(i)
        length -=1
# print(arr) # [['F', 'B'], ['C', 'E'], ['G', 'D'], ['C'], ['A'], [], [], []]
# print(max_length) : 5
# 2번 이상 나오는 알파벳이 있는지 확인

arr = arr[:max_length]  # 필요없는 부분 잘라주기
# arr = [['F', 'B'], ['C', 'E'], ['G', 'D'], ['C'], ['A']]

# 중복해서 나오는것을 어떻게 체크? 자리수에 맞게  A = 9  AAA 111*9 ==> A*(10**2) + A*(10*1)
for i in range(max_length-1,-1,-1):
    for j in arr[i]:
        if j in alpa:
            alpa[j] += 10**i
        else:
            alpa[j] = 10**i

# print(alpa) # {'A': 10000, 'C': 1010, 'G': 100, 'D': 100, 'E': 10, 'F': 1, 'B': 1}

ls = []
for k in alpa:
    ls.append(alpa[k])

ls.sort(reverse=True)

num = 9
result = 0
for i in ls:
    result += i*num
    num -= 1

print(result)




