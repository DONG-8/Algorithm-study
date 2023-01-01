def check(sp):
        stack = []
        while sp:
            a = sp[0]
            if a == "(":
                stack.append(a)
                sp = sp[1:]
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    sp = sp[1:]
                else:
                    return False
        return True


    
def divide_spell(sp):
    bracket = [0,0]
    for s in range(len(sp)):
        if sp[s] == "(":
            bracket[0] += 1
        else:
            bracket[1] += 1
        
        if same_count(bracket):
            return s
        
def same_count(arr):
    if arr[0] == arr[1]:
        return True
    else:
        return False

def flip_bracket(sp):
    word = ""
    for s in sp:
        if s == "(":
            word += ")"
        else:
            word += "("
    return word
    
def recur(sp):
    if not sp:
        return ""
    n = divide_spell(sp)
    # 나누기
    u,v = sp[:n+1],sp[n+1:]
    
    if check(u):
        word = u + recur(v)
    else:
        # u가 올바른 문자열이 아닐때,
        word = "(" + recur(v) + ")" + flip_bracket(u[1:-1])
    return word

    
    
def solution(p):
    answer = ''
    # 우선 올바른 괄호 문자열인지 확인
    if check(p):
        return p
    
    answer = recur(p)
    
    return answer



