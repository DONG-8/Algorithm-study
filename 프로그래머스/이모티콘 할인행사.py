# 플러스 가입자 늘리기
# 다음이 판매액 최대

# 1. 플러스 가입자가 많아야함 일단 우선찾기

# 자기가 생각하는 할인 퍼센트 기준으로 다 삼
# 이때, 총 가격의 합이 내가 생각 한 가격보다 크다면 플러스 가입

# 할인률 조합 -> 16000가지 조합이 나옴

def recur(cur,arr,m,combi,per):
    if cur == m:
        a = arr[:]
        combi.append(a)
        return
    
    per = [10,20,30,40]
    for i in range(4):
        arr[cur] = per[i]
        recur(cur+1,arr,m,combi,per)
        arr[cur] = 0

def emoticon_sale_money(sale,emoticons,per):
    
    for i in range(len(emoticons)):
        for j in range(4):
            sale[i][j] = (emoticons[i] *((100 - per[j]))//100)
            
        
def solution(users, emoticons):
    answer = []
    per = [10,20,30,40]
    m = len(emoticons)
    arr = [0] * m
    combi = []
    recur(0,arr,m,combi,per)
    # 이모티콘 길이 만큼의 각 이모티콘마다의 세일 가격 각 인덱스 == 이모티콘 인덱스
    sale = [[0]*4 for _ in range(m)]
    emoticon_sale_money(sale,emoticons,per)
    all_info = []
    for com in combi:
        no = [0,0]
        for i in range(len(users)):
            money = 0
            for c in range(len(com)):
                if users[i][0] <= com[c]: 
                    money += sale[c][(com[c]//10) - 1]
            if money >= users[i][1]:
                no[0] += 1
            else:
                no[1] += money
        all_info.append(no)
    
    all_info.sort(reverse = True,key= lambda x : (x[0],x[1]))
    return all_info[0]