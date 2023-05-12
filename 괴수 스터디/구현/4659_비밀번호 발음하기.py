while True:
    word = input()
    if word == "end":
        break
    
    # 1단계 모음이 없으면 안됨
    gather = "aeiou"
    flag = False    # 진위여부 판별
    # 2개 단위로 묶어서 판별하고싶음 ee,oo
    lcnt = 0 # 자음
    rcnt = 0 # 모음
    gather_flag = False
    for i in range(len(word)):
        # 하나씩 조건을 탐색
        if word[i] in gather:
            rcnt += 1
            lcnt = 0
            gather_flag = True
        else:
            lcnt += 1
            rcnt = 0

        if lcnt == 3 or rcnt == 3:

            flag = True
        
        if i >= 1 and word[i] == word[i-1] and (word[i] != "e" and word[i] != "o"):
            flag = True
    
    if gather_flag == False or flag == True:
        print("<" + word +"> is not acceptable.")
    else:
        print("<"+word+"> is acceptable.")
