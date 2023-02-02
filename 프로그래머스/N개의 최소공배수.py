def GDC(a,b):
    while a %b != 0:
        a,b = b,a%b
    return b

def solution(arr):
    answer = arr[0]
    num = arr[0]
    for i in range(1, len(arr)):
        num = GDC(answer,arr[i])
        answer *= arr[i] // num
    return answer