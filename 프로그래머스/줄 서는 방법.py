from math import factorial
def solution(n, k):
    answer = []
    arr = list(range(1,n+1))
    while n!= 0:
        num = factorial(n-1)
        a = (k-1)//num
        k = k % num
        answer.append(arr.pop(a))
        n -= 1
    return answer