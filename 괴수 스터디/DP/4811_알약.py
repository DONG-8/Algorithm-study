
# 종료가 될 수 있는 경우
# 1. w가 0이 되어 뒤에는 h만 나오는 경우
# 2, w==0 return 1
# 3. h == -1 return 0
# 4. w == -1 return 0

def recur(w,h):
    if w == -1: return 0
    if h == -1: return 0
    if w == 0:
        return 1
    if dp[w][h] != -1:
        return dp[w][h]
    
    # 계산 
    num = recur(w-1,h+1) + recur(w,h-1)
    dp[w][h] = max(dp[w][h],num)
    return num

while True:
    n = int(input())
    # 행 w 의 갯수, 열 h의 갯수
    dp = [[-1] * ((2*n)+1) for _ in range(n+1)]
    if n == 0:
        break
    else:
        # 실행
        print(recur(n-1,1))
