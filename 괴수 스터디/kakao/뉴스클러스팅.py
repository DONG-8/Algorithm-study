def solution(str1, str2):
    str_1 = {}
    str_2 = {}
    str1 = str1.upper()
    str2 = str2.upper()
    same = {}
    happ = {}


    for i in range(len(str1)-1):
        a = str1[i]+str1[i+1]
        if len(a)==2 and a.isalpha():
            if a in str_1:
                str_1[a] = str_1[a] + 1
            else:
                str_1[a] = 1
          
    for i in range(len(str2)-1):
        a = str2[i]+str2[i+1]
        if len(a)==2 and a.isalpha():
            if a in str_2:
                str_2[a] = str_2[a] + 1
            else:
                str_2[a] = 1
    # print(str_1,str_2)
    happ = str_1.copy()
    # print(happ)
    # 교집합 같은계수 최소값, 교집합 딕
    # 합집합 같은개수 최대값 합집합 딕셔너리 벨류 추가
    # print(str_1)
    for i in str_2:
        if i in str_1:
            same[i] = min(str_1[i],str_2[i])
            happ[i] = max(str_1[i],str_2[i])
        else:
            happ[i] = str_2[i]

    min_num = 0
    max_num = 0
    for x in happ:
        max_num += happ[x]
    for y in same:
        min_num += same[y]
    print(min_num,max_num)

    if min_num == 0 and max_num == 0:
        return 65536
    else:
        return int((min_num/max_num)*65536)

print(solution('FRANCE','french'))



