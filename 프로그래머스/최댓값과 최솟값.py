def solution(s):
    answer = ''
    
    a = list(map(int, s.split(" ")))
    a.sort()
    x,y = min(a),max(a)
    answer = str(x) + " " + str(y)
    return answer