def solution(arrayA, arrayB):
    answer = 0
    
    # 시간복잡도가 크지 않음
    def GDC(a, b):
        while a % b != 0:
            a , b = b , a % b
        return b
    
    # 최대 50만
    def check(arr1,arr2):
        number = 0
        for i in range(len(arr1)):
            number = GDC(number,arr1[i])
        
        for i in range(len(arr2)):
            if arr2[i] % number == 0:
                number = 0
                break        
        return number
    
    a = check(arrayA,arrayB)
    b = check(arrayB,arrayA)
    
    return max(a,b)