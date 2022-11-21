def solution(orders, course):
    answer = []
    combi = []
    check = []
    def recur(word,start,cur,n):
        if cur == n:
            k = check[:]
            k.sort()
            a = ''.join(k)
            combi.append(a)
            return
        
        for i in range(start,len(word)):
            check.append(word[i])
            recur(word,i+1,cur+1,n)
            check.pop()

    # 그냥 무식하게 다 구하기
    
    for word in orders:
        for c in course:
            recur(word,0,0,c)
    
    # print(combi)
    dic = {}
    for cm in combi:
        dic[cm] = dic.get(cm,0) + 1
    
    check = [[] for _ in range(11)]
    # 횟수가 같으면 들어가고, 작으면 있던거 제거, 크면 그대로 킾
    
    # print(dic)
    for wd,cnt in dic.items():
        # wd.sort()
        if cnt >= 2:
            check[len(wd)].append((wd,cnt))
    
    for ar in check:
        if not ar:
            continue
        ar.sort(key = lambda x : -x[1])
        
        max_num = ar[0][1]
        
        for a in ar:
            if a[1] < max_num:
                break
            else:
                answer.append(a[0])
    answer.sort()
    return answer