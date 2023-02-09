def solution(book_time):
    time_table = [0] * (24*61)
    for i in range(len(book_time)):
        start,end = book_time[i]
        start = list(map(int, start.split(":")))
        end = list( map(int, end.split(":")) )
        start_idx = 60 * start[0] + start[1]
        end_idx = 60 * end[0] + end[1] + 10     # 10분 청소시간
        for i in range(start_idx,end_idx):
            time_table[i] += 1
        
    # print(max(time_table))
    return max(time_table)