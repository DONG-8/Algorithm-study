def solution(left, right):
    answer = 0 
    for i in range(left, right + 1):
        count = 0
        
        for k in range(1, i+1):
            if k*k > i:
                break
            if i % k == 0:
                
                if k*k != i :
                    count += 2
                else:
                    count += 1
        
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
        
    
    return answer