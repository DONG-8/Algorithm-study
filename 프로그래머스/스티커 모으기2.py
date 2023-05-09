# n -> 10만?
# 결국 모든 경우를 찾아야함
# 퐁당퐁당이 좋을지, 100,1,1,10000,1 이라면? -> 퐁당퐁당이 항상 옳지가 않음

def solution(sticker):
    answer = 0
    length = len(sticker)
    dp_p = [0] * (length+1)
    dp_m = [0] * (length+1)
    dp_p[1] = sticker[0]
    if length == 1:
        return sticker[0]
    
    for i in range(2, length+1):
        if i != length:
            dp_p[i] = max(dp_p[i-1], dp_p[i-2] + sticker[i-1])
        dp_m[i] = max(dp_m[i-1], dp_m[i-2] + sticker[i-1])
    return max(dp_m[-1],dp_p[-2])