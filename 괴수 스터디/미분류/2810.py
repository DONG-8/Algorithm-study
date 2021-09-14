'''
컵홀더

s 일반 l은 커플석
l은 항상 두개씩 쌍으로 

llsllsssll 8
6 + 2
11 - 3 
ll의 갯수 3개

9
SLLLLSSLL

10 -3

'''

n = int(input())
couple_goto_hell = 0
line = input()

for i in line:
    if i == 'L':
        couple_goto_hell +=1
    
if couple_goto_hell !=0:
    a = int(couple_goto_hell/2)
    print(n-a+1)
else:
    print(n)





