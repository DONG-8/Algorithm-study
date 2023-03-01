def solution(n):
    answer = 0
    is_prime = [True] * (n + 1)             #모두 소수라고 가정

    is_prime[1] = False
    for i in range(2, n + 1):               #2부터 n까지 돌면서 배수 처리.
        if i * i > n:                       #사실 n이 아니라 루트n임
            break

        if not is_prime[i]:                 #i가 소수가 아니면 내 배수는 이미 처리됐을테니 안봄
            continue

        for j in range(i * i, n + 1, i):   #i가 소수인 경우 => i의 배수를 모두 False로 만든다.
            is_prime[j] = False
    
    for i in range(2, n+1):
        if is_prime[i]:
            answer += 1
    
    return answer