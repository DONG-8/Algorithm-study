'''

비트 : 컴퓨터에서 이루는 최소 단위
정수 --> 이진수 표현

비트마스크
이 이진수를 통해 비트연산을 하여 문제를 해결 해 나가는기술

비트 연산을 통한 삽입, 삭제, 조회 등이 간단해짐
더 간결한 코드 작성이 가능
더 빠른 연산이 가능
비트마스크를 이용한 정수 표현으로 DP가 가능함(중요)

'''
import sys
N = input()
S = 0b0
for _ in range(int(N)):
    A = sys.stdin.readline().rstrip().split(" ")

    if A[0] == "add":
        S = S | (1<<int(A[-1]))
    elif A[0] == "remove":
        S = S & ~(1<<int(A[-1]))
    elif A[0] == "check":
        if S & (1<< int(A[-1])):
            print(1)
        else:
            print(0)
    elif A[0] == "toggle":
        S = S ^ (1<<int(A[-1]))
    
    elif A[0] == "all":
        S = 0b111111111111111111111
    else:
        S = 0b000000000000000000000




# a = 0b0
# a =  a | (1 << 2)
# print(a)
# a =  a | (1 << 5)

# print(a)
# print(bin(a))