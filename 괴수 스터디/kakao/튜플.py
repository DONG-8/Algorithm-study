# 중복되는 원소가 없음
# 단, 문자열을 처리해서 튜플별로 묶어주어야함
# 근데 작은 튜플부터 나오는 숫자 순서대로 결과가 나와줘야함

# 1. 문자열 처리
# - 괄호 나오면 내부 튜블 체크 시작
# - 괄호 내부일때, 쉼표가 나오기 전까지는 문자열을 더해줌
# - 쉼표가 나오면 해당 문자열을 에비 배열에 넣어주고, 문자열 초기화
# - 다시 쉼표까지 문자열 더해주기

def solution(s):
    s = s[1:len(s)-1]
    answer = []
    arr = []
    word = ""
    flag = False
    for spell in s:
        # 시작
        if spell == '{':
            flag = True
            continue
        # 닫히면 튜플 초기화
        if spell == '}':
            flag = False
            arr.append(int(word))
            answer.append(arr)
            word = ""
            arr = []
            continue
        
        if flag and spell != ',':
            word += spell
        elif flag and spell == ",": 
            arr.append(int(word))
            word = ""
    
    answer.sort(key = lambda x : len(x))
    result = []
    for tup in answer:
        for i in tup:
            if i not in result:
                result.append(i)
    # print(result)
    return result