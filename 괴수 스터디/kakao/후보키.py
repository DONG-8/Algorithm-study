'''
후보키 : 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성
유일성 --> 릴레이션에 있는 모든 튜플에 대해 유일하게 식별 되어야 한다.
최소성 --> 유일성을 가진 키를 구성하는 속성 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다.
            모든 튜플을 유일하게 식별하는 데 필요한 속성들로만 구성되어야 한다.

구하는 것 : 후보 키의 최대 갯수를 구하라.

'''

# 하나의 info 에 대해서 식별해서 겹치는것이 없다면 후보키의 후보가 될 수 있다.

# 최소성이기 때문에  만약 다음에 하나라도 후보키가 될 수 없는것이 나왔다면 뒤에것 탐색,, 후보키 만들던 리스트 리셋

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# 0인것들끼리 묶어서 봐야함 ... 흠... ㅅㅂ? 걍 첨부터 조합 조지면되는거아닌가?

# set을 이용한 중복 체크 원 길이랑 동일하면 유일성 통과

# 그럼 최소성 체크는? ex) 1,2,3 조합도 유일성 있고, 1,2 유일성 있으면 ? 1 로도 이미 존재하면? 1,2,3의 부분집합들 리스트를 만들고
# 부분집합중 한개가 최종 후보키 리스트에 존재한다면? 그냥 넘겨야함

from itertools import combinations
import itertools

# 각 인덱스 값을 통해서 조합을 받아야함

# 우선 각 열 별 정보를 받아옴
column = [[] for _ in range(len(relation[0]))]

for info in relation:
    # 인포 별 인덱스 순회
    for i in range(len(info)):
        column[i].append(info[i])

# print(column)
# column
#  :[['100', '200', '300', '400', '500', '600'],
#  ['ryan', 'apeach', 'tube', 'con', 'muzi', 'apeach'],
#  ['music', 'math', 'computer', 'computer', 'music', 'music'], ['2', '2', '3', '4', '3', '2']] 열끼리의 정보 분해 완료

# 후보키 정보를 담을 리스트
hubokey = []
# 행별로 조합을 해야함
# 각 인덱스로 접근해서 map을 통해 묶어주기
index_number = list(range(len(relation[0])))
1 
for sss in range(1,1+len(relation[0])):
    # 1개부터 조합해서 인덱스 길이만큼
    combi = itertools.combinations(index_number,sss)
    for numbers in combi: 
        hap = [[] for _ in range(len(column[0]))]
    
        # 조합별로 각 값 합쳐주기 0
        for i in numbers:
            for k in range(len(column[i])):
                hap[k].append(column[i][k])

        hap = list(map(tuple, hap))
       
        if len(hap) == len(set(hap)):
            # 넣기 전에 hubokey에 그 부분집합들이 있는지 확인
            bubun = [] 
            for x in range(1,len(numbers)+1):
                bubun.append(list(itertools.combinations(numbers, x)))
            # bubun에는 bubun집합들이 있음
            # print(bubun,'이게 뿌')
            bubububu = []
            for xxxx in bubun:
                for yyy in xxxx:
                    bubububu.append(yyy)
            
            for huhu in bubububu:
                if huhu in hubokey:
                    break
            else:
                hubokey.append(numbers)

print(len(hubokey))
        
       







'''
# 후보키인지 체크 하기위한 리스트 각 인덱스 별로 하나라도 같은 값이 나온다면, 체크할거임
# check = [1]*(len(relation[0]))
# #체크를 위한 인덱스 별 리스트

# mix_to_combi = []
# # 중복 체크를 통해 check 인덱스 값 == 행 을 중복된것이 있다고 표시

# for info in relation:
#     # 인포 별 인덱스 순회
#     for i in range(len(info)):
#         # i 는 0~~ 8 까지 가능하겠지
#         # 인덱스별 중복 체크를 위한 조건문
#         if info[i] in index_check[i]:
#             # 중복된 값이 있다면 변경
#             check[i] = 0
#             mix_to_combi.append(i)
#             index_check[i].append(info[i])
#         # 없다면?
#         else:
#             # 한 열에 맞는 정보를 각각 append
#             index_check[i].append(info[i])

# # print(mix_to_combi) # [3, 2, 2, 1]
# # print(index_check) # [['100', '200', '300', '400', '500', '600'], ['ryan', 'apeach', 'tube', 'con', 'muzi', 'apeach'], ['music', 'math', 'computer', 'computer', 'music', 'music'], ['2', '2', '3', '4', '3', '2']]

# # print(list(set(mix_to_combi)))
# mix_to_combi = list(set(mix_to_combi))

# # 중복없던것들 바로 갯수 카운트
# count = len(check) - len(mix_to_combi)

'''

