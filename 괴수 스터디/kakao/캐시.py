def solution(cacheSize, cities):
    answer = 0
    ls = []
    for i in cities:
        ls.append(i.lower())

    cities = ls
    cash_list = []
    if cacheSize == 0:
        answer = len(cities)*5
        return answer


    for citi in cities:
        # 리스트에 있음?
        if citi in cash_list:
            answer +=1
            # 참조 되었다면 리스트 가장 마지막으로 보냄
            a =cash_list.pop(cash_list.index(citi))
            cash_list = cash_list + [a]



        # 리스트에 없음?
        else:
            # 리스트 비어있음?
            if len(cash_list) < cacheSize:
                cash_list.append(citi)
                #  cash_list = [citi] + cash_list
                answer += 5
            else:
                # print('내부중복제거')
                cash_list.pop(0)
                answer += 5
                cash_list.append(citi)
                # print('내부중복제거끝')
        
     

    return answer

arr = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
size = 3
print(solution(size,arr))

