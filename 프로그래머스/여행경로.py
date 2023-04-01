from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()
    print(r,'dic')
    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            print(r[q],'갈 수 있는곳이 있음',q)
            s.append(r[q].pop(0))
            print(s,'s')
        else:
            print('갈곳이 없어용')
            p.append(s.pop())
            print(p,'p')
    return p[::-1]




# from collections import deque

# def solution(tickets):
#     answer = []
    
#     # 결국 다 돌아야함
#     arr = [""]*(len(tickets)+1)
#     arr[0] = "ICN"
    
#     info = {}
#     for ticket in tickets:
#         a = info.get(ticket[0],[])
#         a.append([ticket[1],False])
#         a.sort()
#         info[ticket[0]] = a
    
#     # print(info)
#     def dfs(cnt,now,arr):
#         if cnt == len(tickets):
#             k = arr[:]
#             answer.append(k)
#             return
#         if info.get(now,0) == 0:
#             return
        

#         for i in range(len(info[now])):
#             if not info[now][i][1]:
#                 info[now][i][1] = True
#                 arr[cnt+1] = info[now][i][0]
#                 dfs(cnt+1,info[now][i][0],arr)
#                 arr[cnt+1] = ""
#                 info[now][i][1] = False
#     dfs(0,"ICN",arr)
#     answer.sort()
#     return answer[0]