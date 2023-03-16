def solution(n, m, section):
    answer = 0
    # 길이 m 인 포인터를 옮기는 작업
    i = 0
    endpoint = 0
    while i < len(section):
        a = section[i]
        if a  > endpoint:
            endpoint = a + m -1
            answer += 1
        
        i += 1
    return answer