def solution(s):
    answer = 0
    a = s[0]
    x_count = 1
    y_count = 0
    for i in range(1,len(s)):
        if x_count == y_count:
            a = s[i]
            x_count = 1
            y_count = 0
            answer += 1
            continue

        if s[i] != a:
            y_count += 1
        else:
            x_count += 1
    return answer+1