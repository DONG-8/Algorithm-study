def solution(arr):
    answer = []
    a = min(arr)
    if len(arr) == 1:
        return [-1]
    else:
        for n in arr:
            if n == a:
                continue
            else:
                answer.append(n)
        
    return answer