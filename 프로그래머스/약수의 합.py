def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i*i > n:
            break
        if i*i == n:
            answer += n // i
            continue
        if n % i == 0:
            answer += n//i
            answer += i
    return answer