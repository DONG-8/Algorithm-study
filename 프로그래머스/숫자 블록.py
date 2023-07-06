def solution(begin, end):
    answer = [0] * (end-begin+1)
    idx = 0
    for i in range(begin,end+1):
        if i == 1:
            idx += 1
            continue
        check = [1]
        for j in range(2,i+1):
            if j * j > i:
                break

            if i % j == 0:
                if i // j <= 1e7:
                    check.append(i//j)
                if j <= 1e7:
                    check.append(j)
        answer[idx] = max(check)
        idx += 1
    return answer