def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        a = dic.get(s[i],-1)
        if a == -1:
            answer.append(-1)
        else:
            answer.append(i - a)
        dic[s[i]] = i
    return answer