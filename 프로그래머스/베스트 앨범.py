def solution(genres, plays):
    answer = []
    dic = {}
    
    for i in range(len(genres)):
        a = dic.get(genres[i],[[genres[i],0],[]])
        a[0][1] += plays[i]
        a[1].append((i,plays[i]))
        dic[genres[i]] = a
    one = []
    for k in dic.items():
        one.append(k[1][0])
    
    one.sort(reverse = True,key= lambda x : x[1])
    
    for k in one:
        arr = dic[k[0]][1]
        arr.sort(key = lambda x : (-x[1],x[0]))
        if len(arr) >= 2:
            for i in range(2):
                answer.append(arr[i][0])
        else:
            answer.append(arr[0][0])
    
    
    return answer