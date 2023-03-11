def solution(n, m):
    answer = []
    A,B = n,m
    while n % m != 0:
        n, m = m, n%m
    return [m, (A*B)//m]