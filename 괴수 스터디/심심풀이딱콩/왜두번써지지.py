'''
숫자를 2번쓰는 오류
2번써진거 걸러서

44 -> 원래는 4 한번입력

1. 112233 --> 123 으로 바꿔주기
2. 123 -> 이진수로 변경시켜주기

'''

string = input()
num = 0
string_1 = []
for i in range(0,6,2):
    num = string[i]
    string_1.append(num) # ['1'] --> ['1','2'] ==>['1','2','3']
str = int(''.join(string_1)) 

