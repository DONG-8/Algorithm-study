'''
한변의 길이가 1인 정육면체 모양조각 N개로 나눌 수 있어야 한다.
3개의 패턴을 가진 띠를 딱 맞게 두를 수 있어야 한다.
1조각당 부피 1
높이 1

'''

# 입력

T = int(input())

for t in range(T):
    N = int(input())

    if N%3 == 2 or N%9 == 0:
        print("TAK")
    else:
        print("NIE")
