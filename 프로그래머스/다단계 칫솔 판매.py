from collections import defaultdict
import math
def solution(enroll, referral, seller, amount):
    answer =[]
    # 초기 money 보유 량
    money = defaultdict(int)
    answer_dic = defaultdict(int)
    par_dic = defaultdict(str)
    for v in range(len(seller)):
        money[seller[v]] = amount[v] * 100
    
    for idx in range(len(referral)):
        par_dic[enroll[idx]] = referral[idx]
    
    for i in range(len(seller)):
        son = seller[i]
        upper_money = amount[i] * 100
        while son != "-":
            if upper_money == 0:
                break
            # 판매를 통해 내 자식이 얻은 금액
            my_money =upper_money -  int(0.1 * upper_money)
            upper_money = int(0.1 * upper_money)
            answer_dic[son] += my_money
            son = par_dic[son]
    
    # print(answer_dic)
        
    # 하나의 값을 찾았을 때 하나씩 그냥 위로 가게 해야겠다 더해지는 값을 미리 다 올리고 
    for i in range(len(enroll)):
        answer.append(int(answer_dic[enroll[i]])) 
    
    return answer