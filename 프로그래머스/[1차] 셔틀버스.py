def solution(n, t, m, timetable):
    answer = ''
    # 시간은 분으로 전환
    shuttle_time = 540 # 9시부터 시작임
    idx = 0
    timetable.sort()
    for i in range(n):
        shuttle = []
        while idx < len(timetable) and len(shuttle) < m:
            hour, minute = list(map(int,timetable[idx].split(":")))
            minute = hour * 60 + minute
            if minute <= shuttle_time:
                shuttle.append(minute)
                idx+= 1
            else:
                break
        if shuttle and len(shuttle) == m:
            answer = shuttle[-1] -1
        else:
            answer = shuttle_time
        shuttle_time += t
    return "%02d:%02d" %(answer//60,answer%60)