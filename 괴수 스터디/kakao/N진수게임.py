

# 진수별 변경법

# 진수에 상관없이 접근할 수 있는 리스트 만들기


n = 16

# 말해야 하는 길이
t = 16

# 플레이어수
m = 2

# 튜브의 순서
p = 2

def division(num,n):
    num_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    a = num%n
    b = num//n

    if b != 0:
        return division(b,n) + num_list[a]
    else:
        return num_list[a]

result = ''
for num in range(t*m):
    result += division(num,n)

    # 모든 플레이어가 말하는 횟수만큼의 길이의 모든 문자열을 가져온다.
    # if len(result) == t*m:
    #     break

# 자기순서 + M*I 번째의 스트링만 가져온다.
final = ''
for i in range(p-1,len(result),m):
    final += result[i]

    # if len(final) == t:
    #     break

print(final)
    
    
    # 리턴된 리스트

    # 여기서 종료조건
