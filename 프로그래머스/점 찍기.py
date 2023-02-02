import math
def solution(k, d):
    answer = 0
    for i in range(d+1):
        if d**2 < (i*k) **2:
            break
        y = math.sqrt(d**2 - (i*k)**2)
        answer += int(y)//k+1

    return answer