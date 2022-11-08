def solution(number):
    answer = 0
    arr = []
    def recur(start,cur,combi):
        
        if cur == 3:
            a = combi[:]
            arr.append(a)
            return
        
        for i in range(start,len(number)):
            combi.append(i)
            recur(i+1,cur+1,combi)
            combi.pop()
    
    recur(0,0,[])
    
    for a,b,c in arr:
        k =  number[a] + number[b] + number[c]
        if k == 0:
            answer += 1
    
    return answer