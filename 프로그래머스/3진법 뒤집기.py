def solution(n):
    answer = 0
    three = ""
    while n:
        b = n %3
        n = n //3
        three += str(b)

    for i in range(len(three)):
        answer += int(three[i]) * (3 ** (len(three) - i-1))
        
    return answer