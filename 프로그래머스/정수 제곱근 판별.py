import math
def solution(n):
    sqrt = math.sqrt(n)
    if sqrt != int(sqrt):
        return -1    
    return (sqrt+1)**2