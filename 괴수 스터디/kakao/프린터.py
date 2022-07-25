def solution(priorities, location):
    answer = 0
    count = 1
    while True:
        max_num = max(priorities)
        # 가장 큰 값 확인,
        for i in range(len(priorities)):
            if priorities[i] == 0:
                continue
            if max_num == priorities[i]:
                priorities[i] = 0
                
                if i == location:    
                    return count
                else:
                    max_num = max(priorities)
                count += 1
    return answer