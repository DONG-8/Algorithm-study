def solution(want, number, discount):
    original_want = {}
    check = {}
    count = 0
    
    for i in range(len(want)):
        original_want[want[i]] = number[i]

    for k in range(len(discount[:10])):
        check[discount[k]] = check.get(discount[k],0) + 1
    
    if check == original_want:
        count += 1
    
    for i in range(len(discount) - 10):
        check[discount[i]] = check[discount[i]] - 1
        
        if check[discount[i]] == 0:
            del(check[discount[i]])
        
        check[discount[i+10]] = check.get(discount[i+10],0) +1
        if check == original_want:
            count += 1
    
    return count