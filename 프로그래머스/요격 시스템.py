def solution(targets):
    targets.sort(key = lambda x : x[1])
    # 시작점을 기준
    end = 0
    count = 0
    for s,e in targets: 
        if s < end:
            continue
        else:
            end = e
            count += 1
    
    return count