def solution(n, left, right):
    # 시간복잡도는 O(n)인데 n이 너무 큼 -> 10^7
    # 규칙 찾아야함
    answer = []
    # i, j의 값중 큰 값의 +1이 해당 열의 값 
    
    for i in range(left,right+1):
        num  = max(i//n, i % n)
        answer.append(num+1)
    return answer