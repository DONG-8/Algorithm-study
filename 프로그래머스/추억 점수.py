def solution(name, yearning, photo):
    answer = []
    info = {}
    for i in range(len(name)):
        info[name[i]] = yearning[i]
    
    for arr in photo:
        point = 0
        for n in arr:
            a = info.get(n,"")
            if a != "":
                point += a
        answer.append(point)
    return answer