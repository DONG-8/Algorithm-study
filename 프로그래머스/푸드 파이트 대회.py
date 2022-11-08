def solution(food):
    answer = ''
    # 2보다 작으면 사용 x
    
    for i in range(1,len(food)):
        num = food[i]
        if num < 2:
            continue
        else:
            a = num // 2
            str_num  = str(i)*a
            answer += str_num
    reverse = answer[::-1]
    
    answer = answer + "0" + reverse
    
    return answer