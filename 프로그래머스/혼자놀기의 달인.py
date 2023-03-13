# def find(x,visit):
#     if visit[x] == x:
#         return x
#     else:
#         visit[x] = find(visit[x],visit)
#         return visit[x]

# def union(x,y,visit):
#     x = find(x,visit)
#     y = find(y,visit)
    
#     visit[y] = x


# def solution(cards):
#     answer = 0
#     max_num = 0
    
#     visit = list(range(len(cards)))
    
#     for i in range(len(cards)):
#         union(visit[i],visit[cards[i]-1],visit)
    
#     for i in range(len(cards)): 
#         find(i, visit)
#     dic = {}
#     for k in range(len(visit)):
#         a = dic.get(visit[k],0)
#         dic[visit[k]] = a + 1

#     arr = []
    
#     for i,v in dic.items():
#         arr.append((v,i))
#     if len(arr) == 1:
#         return 0
#     arr.sort(reverse= True)
    
    
#     return arr[0][0] * arr[1][0]


def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
        
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])