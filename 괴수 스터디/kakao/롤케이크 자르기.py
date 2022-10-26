def solution(topping):
    answer = 0
    left_arr = [0]*10001
    right_arr =[0]*10001
    # 한번 기록 -> 
    for tp in topping:
        right_arr[tp] += 1
    
    left_count = 0
    right_count = len(right_arr) - right_arr.count(0)
    
    for i in range(len(topping)):
        # 토핑 번호를 가져옴
        tp = topping[i]
        # 어짜피 없는걸 빼지는 않음 갯수만 체크
        left_arr[tp] += 1
        right_arr[tp] -= 1
        
        if left_arr[tp] == 1:
            left_count += 1
        
        if right_arr[tp] == 0:
            right_count -= 1
        
        # 검증
        if left_count == right_count:
            answer += 1
        
    return answer