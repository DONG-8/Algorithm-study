def recur(arr,visit,result,sol_length,n):
    
    if sol_length == n:
        if len(set(visit)) == sol_length and set(visit) not in result:
            result.append(set(visit))
            
        return
    
    for num in range(len(arr[n])):
        visit.append(arr[n][num])
        recur(arr,visit,result,sol_length,n+1)
        visit.pop()


            
def solution(user_id, banned_id):
    answer = 0
    
    arr = [[] for _ in range(len(banned_id))]
    sol_length = len(banned_id)
    
    for i in range(len(banned_id)):
        length = len(banned_id[i]) # 길이 체크 "***" 와같은 경우를 위해서
        for j in user_id:
            # 길이가 다를경우 볼 필요도 없음
            if len(j) != length:
                continue
        
            # 동일한지 확인하기 위한 count
            count = 0
            for k in range(len(j)):
                if banned_id[i][k] == "*":
                    count += 1
                else:
                    if banned_id[i][k] == j[k]:
                        count += 1
                    else:
                        break
            else:
                # 벤된 아이디와 *을 제외하고 동일한경우
                # 해당 순서의 배열에 추가시켜준다.
                arr[i].append(j)
                
    
    result = []
    visit = []
    recur(arr,visit,result,sol_length,0)
    
    return len(result)
