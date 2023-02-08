def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    i,j = 0,0
    while j < len(B):
        if A[i] >= B[j]:
            j += 1
        else:
            i += 1
            j += 1
            answer += 1
    return answer