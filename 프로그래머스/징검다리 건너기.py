def solution(stones, k):
    # 이분탐색 해야지뭐
    l,r = 1,200000000
    length = len(stones)
    while l <= r:
        flag = False
        mid = (l+r)//2
        cnt = 0
        for i in range(length):  
            if stones[i] - mid <= 0:
                cnt += 1
            else:
                cnt = 0      
            if cnt == k:
                break
        if cnt == k:
            r = mid - 1
        else:
            l = mid + 1   
    return l