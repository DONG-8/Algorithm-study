# 찾아가는거지.. 
# 계속 2등분 하는 길이로 for문 탐색
# 만약 다 같은 숫자라면 같은 경우라면 +1 하고
# 끝까지 가서 1이면
# 결국 n은 10임 재귀 가능    
def solution(arr):
    # 처음에는 숫자 값이 아무것도 없음
    answer = [0,0]
    num = 0
    # 첫번째 길이 탐색
    def recur(n, start):
        if n == 1:
            answer[arr[start[0]][start[1]]] += 1
            return
        # 검증
        num = arr[start[0]][start[1]]
        tag = True
        for i in range(start[0],start[0]+n):
            for j in range(start[1],start[1]+n):
                if arr[i][j] != num:
                    tag = False
                    break
            if tag == False:
                break
        
        if tag == True:
            answer[num] += 1
            return
        else:
            for i in range(start[0],start[0]+n,n//2):
                for j in range(start[1],start[1]+n,n//2):
                    recur(n//2, (i,j))
        
    
    recur(len(arr),(0,0))
        
    
    return answer