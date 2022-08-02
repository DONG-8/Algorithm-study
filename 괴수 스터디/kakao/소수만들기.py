def solution(nums):
    answer = 0
    # 주어진 수에서 3개의 수를 더해야함,
    # 중복된 숫자가 없음.
    # 순서 상관없이 중복이 없는 3개로 만든 조합
    arr = []
    result = []
    recur(0,0,nums,arr,result)
    
    return len(result)

def recur(cur,start,nums,arr,result):
    
    if cur == 3:
        a = sum(arr)
        if sosu(arr): result.append(1)
        return
    
    
    for i in range(start,len(nums)):
        arr.append(nums[i])
        recur(cur +1,i+1,nums,arr,result)
        arr.pop()
        
        
def sosu(arr):
    n = sum(arr)
    # 소수구하기
    for i in range(2, n):
        if i * i > n:
            break

        if n % i == 0:
            return False
    return True
            