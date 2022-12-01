def solution(k, tangerine):
    answer = 0
    # 크기별로 분류했을 때, 서로 다른 종류의 수를 최소화
    
    # 갯수가 많은 것 부터 정렬 갯수 포함 정렬
    dic = {}
    for size in tangerine:
        a = dic.get(size,0) + 1
        dic[size] = a
    arr = []
    for key,value in dic.items():
        arr.append((key,value))

    # 많은 것 부터 정렬
    arr.sort(key=lambda x : -x[1])
    count = 0
    kk = 0
    for x,y in arr:
        count += 1
        kk += y
        if kk >= k:
            break 
    
    return count