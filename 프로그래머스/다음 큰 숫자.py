def solution(n):
    answer = 0
    flag = True
    print((bin(n)))
    count =0
    for i in bin(n):
        if i == "1":
            count +=1 
    while flag:
        next_count = 0
        
        n += 1
        
        for i in bin(n):
            if i == '1':
                next_count += 1
        
        if next_count == count:
            flag = False
            answer = n
    return answer