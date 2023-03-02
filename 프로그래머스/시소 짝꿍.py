def solution(weights):
    answer = 0
    # 가능한 작은 수에서의 거리비율
    # 나보다 큰 값에 대한 쌍만 찾는다 -> 중복이 제거됨
    dis_combi = [(3,2),(4,2),(4,3)]
    dic = {}
    # 일단 몸무게의 종류 수집 10만
    for weight in weights:
        a = dic.get(weight,0)
        dic[weight] = a+1
    
    # 1보다 그면 같은게 2개니까
    for k,v in dic.items():
        # value가 1보다 크다면 나랑 무게가 같은사람이 n명 이로 만드는 2쌍 조합
        if v > 1:
            answer += (v * (v-1)) // 2
        
        for i in range(3):
            try:
                # 다른 value로 구한 값에 대해서 값이 있는지 찾는다
                a =k * dis_combi[i][0] / dis_combi[i][1]
                answer += dic[a] * v
            except:
                continue
    return answer
