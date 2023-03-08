def solution(n, stations, w):
    answer = 0
    arr = []
    start = 1
    for num in stations: 
        ss = num - w
        if ss >=1:
            arr.append(ss-start)
        start = num + w + 1
    
    if start <= n:
        arr.append(n - start + 1)
        
    for i in arr:
        answer += i // (w*2 + 1)
        if i % (w*2 + 1) != 0:
            answer += 1
    return answer