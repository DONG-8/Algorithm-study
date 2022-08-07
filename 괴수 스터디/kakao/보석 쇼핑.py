# 이진탐색으로 풀어야함.

def solution(gems):
    answer = [0,len(gems)-1]
    # 근본 투포인터
    dic = {}
    # 처음에 값 추가
    dic[gems[0]] = 1
    s,e = 0,0
    # 보석종류 갯수
    gem_kind= len(set(gems))
    # 끝점까지 가면서 다 탐색하셈
    while s < len(gems) and e < len(gems):
        
        # e 포인터를 움직이는 조건, 보석종류를 다 포함할때까지,
        if len(dic) < gem_kind:
            e += 1
            if e == len(gems):
                break
            dic[gems[e]] = dic.get(gems[e],0) + 1
        
        # 다 포함했을때 s 포인트 늘려주기
        else:
            # s,e 포인트가 기존의 answer의 길이보다 작다면, 추가
            if (answer[1]-answer[0]) > e - s:
                answer = [s,e]
            
            # 스타트 포인트를 늘리기 전, 이제 포함되는 보석에서 제거해야함
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1
    
    answer[0] += 1
    answer[1] += 1
    return answer



# sstop, estop = False, False
#     # 투포인터
#     while s <= e:
#         if sstop == True and estop == True:
#             break
#         # 끝점부터 탐색시작
#         if estop == False:
#             b = dic[gems[e]]
#             if b - 1 > 0:
#                 dic[gems[e]] -= 1
#                 e -= 1
#             else:
#                 estop = True
#         else:
#             a = dic[gems[s]]
#             if a - 1 > 0:
#                 dic[gems[s]] -= 1
#                 s += 1
#             else:
#                 sstop = True     
                
#     answer = [s+1,e+1]