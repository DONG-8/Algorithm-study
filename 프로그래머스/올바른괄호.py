def solution(s):
    answer = True
    q = []
    for i in s:
        if i == "(":
            q.append(i)
        else:
            if q:
                length = len(q)
                a = q.pop()
                if a == "(":
                    continue
                else:
                    return False
            else:
                return False
            
    if q:
        return False
    else:
        return True
    return True