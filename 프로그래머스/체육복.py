def solution(n, lost, reserve):
    student = [0]*n
    # 한벌만 가진 학생의 수를 체크한다
    
    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    reserve = list(set_reserve)
    lost = list(set_lost)
    
    one_training_cloth = n - len(lost) - len(reserve)
    # 학생복을 여벌로 가지고 있는 사람을 체크한다.
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i-1)
        elif i + 1 in lost:
            lost.remove(i+1)
    
    answer = n - len(lost)
    return answer
    