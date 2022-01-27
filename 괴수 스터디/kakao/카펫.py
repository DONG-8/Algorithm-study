def solution(brown, yellow):
    total_block = brown + yellow
    # 가로가 더 길다
    # 최소 3칸까지 가야함
    for garo in range(total_block,2,-1):
        if total_block % garo == 0:
            sero = total_block//garo
            # 둘러싼것 검증
            if (sero-2)*(garo-2) == yellow:
                return [garo,sero]