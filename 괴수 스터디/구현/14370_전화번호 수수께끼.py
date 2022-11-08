T = int(input())
number = [
    ('Z','ZERO',0),
    ('X','SIX',6),
    ('G','EIGHT',8),
    ('S','SEVEN',7),
    ('V','FIVE',5),
    ('F','FOUR',4),
    ('I','NINE',9),
    ('W','TWO',2),
    ('R','THREE',3),
    ('O','ONE',1)
]

for t in range(T):
    # 테스트케이
    word = input()
    # 구분
    # 반복해서 문자열을 제거해야함
    dic = {}
    for i in word:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    arr = []
    # 이 키를 이용하여 중복없이 특별한 키 영어를 가진 값부터 제거
    for spell,st_num,int_num in number:
        if dic.get(spell,0) > 0:
            spell_count = dic[spell]
            for sp in st_num:
                dic[sp] -= spell_count
            
            for i in range(spell_count):
                arr.append(int_num)
    arr.sort()
    result = ""
    for i in arr:
        result += str(i)
    
    print('Case #{}: {}'.format(t+1,result))
    
    
    


# i = 0
#     while i <= 9:
#         while True:
#             flag = False
#             for spell in number[i]:
#                 if spell in dic and dic[spell] >= 1:
#                     continue
#                 else:
#                     flag = True
            
#             if flag == True:
#                 break
#             else:
#                 spell_count = {}
#                 for sp in number[i]:
#                     if sp in spell_count:
#                         spell_count[sp] += 1
#                     else:
#                         spell_count[sp] = 1
                
#                 check = False
#                 # 체크 완료 되었음
#                 # 여기서 이 갯수보다 남아있는 갯수가 안되면 넘김
#                 for key,sp in  spell_count.items():
#                     if dic[key] < sp:
#                         check = True
#                         break
                
#                 if check == True:
#                     break
#                 else:
#                     for key,sp in spell_count.items():
#                         dic[key] -= sp
                    
#                     arr.append(i)
#         i += 1                
#     result = ""
#     arr.sort()
#     for i in arr:
#         result += str(i)