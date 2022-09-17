def solution(s):
    answer = -1
    # 문자열 이동 길이  == s 길이
    count = 0
    
    # 연속 닫힌거? 좌괄호가 나오면 계속 가
    key = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }

    for i in range(len(s)):
        if i == 0:
            rotate_s = s
        else:
            # 배열 바꾸기 몇번째까지? 나누느냐는 idx로 접근
            rotate_s = s[i:] + s[0:i]
        
        # 배열이 바뀜 여기서 이제 짝이 맞는지 확인해야함
        # stack q 방식으로 체크
        q = []
        for j in range(len(s)):
            if rotate_s[j] == "]" or rotate_s[j] == ")" or rotate_s[j] == "}":
                if q:
                    pop_s = q.pop()
                    if key[pop_s] == rotate_s[j]:
                        continue
                    else:
                        q.append(rotate_s[j])
                        break
                else:
                    q.append(rotate_s[j])
                    break
            else:
                q.append(rotate_s[j])
                
        if not q:
            count +=1
    
    return count