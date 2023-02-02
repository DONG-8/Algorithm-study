import math
def solution(w,h):
    answer = 0
    num = 0
    # 기울기에 따른 교점 위치가 나옴,
    # 예시 3/2 ->
    def GDC(a,b):
        
        while a%b != 0:
            a,b = b, a % b
        
        return b
    k = GDC(w,h)
    
    answer = w*h - (w+h- k)
    
    return answer