def solution(clothes):
    # 경우의 수 문제인 것 처럼 보인다.
    dic = {}
    case = 0
    # 문자열 처리
    for cloth in clothes:
        wear, cat = cloth[0],cloth[1]
        a = dic.get(cat,[])
        a.append(wear)
        dic[cat] = a

    arr = []
    num = 1
    for key,val in dic.items():
        num *= len(val)+1

    num -= 1


    return num