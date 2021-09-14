'''
문자열을 앞에서 부터 차례대로 출력 할려고 한다.

ZOAC

26

LBOLVUEEPMOIENMG

100
'''

alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# 아스키 코드도 가능
# 'ABCDEFGHIJKLMNOP'

n = input()
n = 'A' + n
sum_of_num = 0

for i in range(len(n)-1):
    # z가 들어왔구만
    a = abs(alpa.index(n[i]) - alpa.index(n[i+1]))
    b = 25 - abs(alpa.index(n[i+1]) - alpa.index(n[i])) + 1
    if a > b:
        sum_of_num += b
    elif a <= b:
        sum_of_num += a

print(sum_of_num)

# 추가수정