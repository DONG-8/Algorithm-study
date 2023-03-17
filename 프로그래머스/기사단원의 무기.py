def div(num):
    count = 0
    
    for i in range(1, num+1):
        if i*i > num:
            break
        
        if num % i == 0:
            if i*i == num:
                count += 1
            else:
                count += 2
    
    return count

def solution(number, limit, power):
    answer = 0
    weight = [power] * number
    # 약수의 갯수 구하기
    for i in range(1, number+1):
        a = div(i)
        if a <= limit:
            weight[i-1] = a
    # limit 과 비교  
    return sum(weight)