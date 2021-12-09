# 숫자 포함 정렬                                                                      
def solution(files):
    int_test_case = ['0','1','2','3','4','5','6','7','8','9']
    ls = []
    number_check = False
    tail_check = False
    
    for k in files: 
        head = ''
        number = ''
        tail = '' 
        for i in k:
            if i not in int_test_case and number_check == False and tail_check == False:
                head += i
            
            elif i in int_test_case and len(number) <= 5 and tail_check == False:
                number_check = True
                number += i
            
            elif number_check == True:
                tail_check = True
                tail += i
        
        number_check = False
        tail_check = False
        ls.append([head,number,tail])

    # 문자열 기준 정렬
    ls.sort(key= lambda x : (x[0].lower(),int(x[1])))
    result = []
    for i in ls:
        result.append(''.join(i))


    return result



# --- head , number, tail 분리
# a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# a.sort(

# )
# b = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

# print(b)
# int_test_case = ['0','1','2','3','4','5','6','7','8','9']
# ls = []
# number_check = False
# tail_check = False
 
# for k in b: 
#     head = ''
#     number = ''
#     tail = '' 
#     for i in k:
#         if i not in int_test_case and number_check == False and tail_check == False:
#             head += i
        
#         elif i in int_test_case and len(number) <= 5 and tail_check == False:
#             number_check = True
#             number += i
        
#         elif number_check == True:
#             tail_check = True
#             tail += i
    
#     number_check = False
#     tail_check = False
#     ls.append([head,number,tail])

# print(ls)
# # 문자열 기준 정렬
# ls.sort(key= lambda x : (x[0].lower(),int(x[1])))
# result = []
# for i in ls:
#     result.append(''.join(i))

# print(result)






# for j in range(len(ls)):
#     # 하나의 헤드 값 가져오기
#     string = ls[j][0]
#     for i in range(j+1,len(ls)):

#         # 첫번째 문자열과 두번째 문자열이 다르다면 패스
#         # 다르다면?
    
#         if string == ls[i][0].upper():
#             if int(ls[j][1]) > int(ls[i][1]):
#                 ls[i], ls[j] = ls[j], ls[i]
#                 print('조건 통과, 현 리스트 배열은 : {}'.format(ls))
#                 print()
#             pass
            



# number 끼리 확인 --> int 처리 해 준다.

# head 기준 정렬

# 그 안에서 같은 문자라면



