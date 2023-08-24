def solution(n):
    return hanoi(n, 1, 3, [])

def hanoi(n, a, b, history): # n개, a -> b
    if n == 0: return
    
    hanoi(n-1, a, 6-(a+b), history)
    history.append([a, b])
    hanoi(n-1, 6-(a+b), b, history)
    
    return history

## 재귀 규칙을 통해 bottom up 방식으로 이루어진다.