from collections import deque

def solution(plans):
    answer = []
    # 시간은 계산하기 쉽게 분으로 변경
    time = 0 # time 최대 1440
    stop =deque([])
    
    # (과목, 남은시간) 시간 기준으로 que 또는 새로운 과목인지
    # 멈춘 과제가 여러개일경우 가장 최근에 멈춘 과제부터
    
    time_table = [() for _ in range(98701)]
    for name,start, playtime in plans:
        h, m = start.split(":")
        start_time = int(h) * 60 + int(m)
        time_table[start_time] = (name,int(playtime))
    
    # 기존 과제의 시간을 감소하고 있는지 체크
    now_time = 0
    now_name = ""
    Flag = False
    while time <= 98700:
        if time_table[time]:
            if Flag:
                stop.append((now_name,now_time))
                print(now_name,now_time)
            now_name, now_time = time_table[time]
            Flag = True
        
        if not Flag and stop:
            now_name, now_time = stop.pop()
            Flag = True
            
        time += 1
        now_time -= 1
        
        if now_time == 0 and Flag:
            answer.append(now_name)
            Flag = False
    return answer