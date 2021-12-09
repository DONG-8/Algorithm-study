'''
무손실 압축 알고리즘

LZW 압축 구현

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화 한다.



'''

def solution(msg):
    alpa = [0,'A','B',"C","D",'E','F','G',
        'H','I','J','K','L','M','N',
        'O','P','Q','R','S','T',
        'U','V','W','X','Y','Z',]

    word = msg
    result  = []
    # print(alpa.index('A'))
    # 현 문자와 다음 문자를 확인해야함
    # 그런데? 다 붙어서 이미 나온경우는 어쩔건데? 이거지
    # now 와 next를 알기 위한 for문
    now = word[0]
    count = 0
    for j in range(len(word)):

        # 마지막 단어는 그냥 넣어주쎄옹
        if j == len(word)-1:
                result.append(alpa.index(now))
                break

        # print(j,'번째단어')
        if now + word[j+1] in alpa:
            # print('있는단어이기때문에 넘기겠습니다')
            now += word[j+1]
            # print(now,'now를 갱신했습니다')


        else:
            # print('값이 없을때')
            
            c = word[j+1]
            result.append(alpa.index(now))
            wc = now + c
            # print('사전에 추가될 단어 :', wc)
            alpa.append(wc)
            now = c

    return result


# alpa = [0,'A','B',"C","D",'E','F','G',
#         'H','I','J','K','L','M','N',
#         'O','P','Q','R','S','T',
#         'U','V','W','X','Y','Z',]

# word = 'ABABABABABABABAB'
# result  = []
# i = 0
# # print(alpa.index('A'))
# # 현 문자와 다음 문자를 확인해야함
# # 그런데? 다 붙어서 이미 나온경우는 어쩔건데? 이거지
# # now 와 next를 알기 위한 for문
# now = word[0]
# count = 0
# for j in range(len(word)):


#     print(j,'번째',now)

#     if j == len(word)-1:
#             result.append(alpa.index(now))
#             break

#     # print(j,'번째단어')
#     if now + word[j+1] in alpa:
#         # print('있는단어이기때문에 넘기겠습니다')
#         now += word[j+1]
#         # print(now,'now를 갱신했습니다')


#     else:
#         # print('값이 없을때')
        
#         c = word[j+1]
#         result.append(alpa.index(now))
#         wc = now + c
#         # print('사전에 추가될 단어 :', wc)
#         alpa.append(wc)
#         now = c

# print(result)


# 만약 사전추가를 하려고 했던 단어가, 이미 사전에 있다면?!
# 이거를 현재 입력으로 바꿔줌

    



# 만약 두개를 합친게 있다면 바로 그걸 찾게 해야하고
#

# 두개를 합친게 없다면 따로 따로 해서 진행 대신 

