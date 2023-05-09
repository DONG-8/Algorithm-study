def solution(picks, minerals):
    answer = 1000000000
    length = len(minerals) // 5
    if len(minerals) % 5 != 0:
        length += 1
    # 조합에 따라 넣어줄 값
    memo = ([-1]*5)*length
    combi = []
    def make_arr(cur,info):
        cur = cur * 5
        memo[cur:cur+5] = [info] * 5
    
    def reset_arr(cur,info):
        cur = cur * 5
        memo[cur:cur+5] = [-1] * 5    
    
    def find_combinations(cur,picks):
        # 곡굉이가 없거나
        if sum(picks) == 0 or cur == length:
            combi.append(memo[:])
            return
        
        for i in range(3):
            if picks[i] != 0:
                picks[i] -= 1
                make_arr(cur,i)
                find_combinations(cur+1,picks)
                reset_arr(cur,i)
                picks[i] += 1
    
    find_combinations(0,picks)
    
    # combi에는 이제 사용된 곡굉이의 정보가 들어가있다.
    # minerals 합쳐서 사용 대신 짧은 길이꺼만큼만 갈 수 있게 길이를 구함    
    stress = [[1,1,1],[5,1,1],[25,5,1]]

    info = {
        "diamond" : 0,
        "iron" : 1,
        "stone" : 2
    }
    
    number_minerals = [-1] * len(minerals)
    for i in range(len(minerals)):
        number_minerals[i] = info[minerals[i]]
    for com in combi:
        stress_num = 0
        for i in range(len(minerals)):
            if com[i] != -1:
                stress_num += stress[com[i]][number_minerals[i]]
        answer = min(stress_num, answer)            
    
    return answer