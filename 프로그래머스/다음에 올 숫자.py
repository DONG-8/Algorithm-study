def solution(common):
    answer = 0
    # 등차인지 등비인지 구분해야함
    # 하나의 수에 대해서 0,1번을통한 등차 등비일때의 값을 알아내야함
    
    # 등차라면
    diff = common[1] - common[0]
    if common[2]  == diff + common[1]:
        answer = common[len(common) -1] + diff
        return answer
    else:
        answer = common[len(common) -1] * (common[1]//common[0])
        return answer    
    return answer
    