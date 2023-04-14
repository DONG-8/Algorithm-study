def solution(sequence, k):
    answer = [0,999999999999999]
    hap = 0
    l,r = 0,0
    while True:
        if l == len(sequence) and r == len(sequence):
            break
        
        if hap < k and r < len(sequence):
            hap += sequence[r]
            r += 1
        else:
            if hap == k:
                length = r-l
                if length < answer[1]+1 - answer[0]:
                    answer = [l,r-1]
            hap -= sequence[l]
            l += 1
    return answer