from itertools import combinations as cb

def solution(nums):
    answer = 0
    
    result = []
    for numb in cb(nums, int(len(nums)/2)) :
        result.append(len(set(numb)))
    
    answer = max(result)

    return answer