# 배열길이 20만
# 1시간 작업량 1
# works의 원소 각 일의 작업량
# 피로도"를" 최소화 시켜야합
# n시간동안 일을 처리해야합니다

# 제일 큰 값이 없을 때 큰 값 기준으로 하나씩 빼내 줘야함

# works의 길이 2만 * n 100만 복잡도에서 시간 효율성 초과
# 2만 for문을 통해 count
# 각 숫자들의 크기별로 나온 값의 배열 -> 최대 5만 정렬하면 시복 ㄱㅊ
# 그리고 갯수 카운팅 list로 가장 큰 배열의 값에서 하나씩 제거
import heapq

def solution(n, works):
    answer = 0
    dic = {}
    # 갯수 저장 + 최대값 찾기위한 배열 찾기
    num_list = []
    for num in works:
        a = dic.get(num, 0)
        dic[num] = a + 1
        if num not in num_list:
            num_list.append(-num)
    
    # n의 값이 있을 동안, 값을 빼준다.
    # 대신 배열에서 뽑아낸 최대 값이 0일경우 answer = 0
    # max_num 에서 1을 뺀 값이 0 이라면 break -> 일을 다 했다는 얘기임
    # 각 최고의 값을 빼내기 위해선 heap을 사용하여 정렬하는과정을 최적화 할 필요가 있어보임
    heapq.heapify(num_list)
    while num_list and n:
        a = heapq.heappop(num_list)
        if a >= 0:
            break
        a *= -1
        # 현재 최대 값
        count = dic[a]
        if count <= n:
            n -= count
            k = dic.get(a-1, 0)
            dic[a] = 0
            dic[a-1] = k + count
            heapq.heappush(num_list,-(a-1))
        else:
            dic[a] = dic[a] - n
            dic[a-1] = dic.get(a-1,0)+ n
            n = 0
        
        
    for key,value in dic.items():
        if key <= 0:
            break
        answer += (key**2) * value
    
    return answer