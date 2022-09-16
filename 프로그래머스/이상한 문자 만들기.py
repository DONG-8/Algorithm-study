def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if count % 2 == 0 and s[i] !=" ":
            answer += s[i].upper()
            count += 1
        elif count % 2 == 1 and s[i] !=" ":
            answer += s[i].lower()
            count += 1
        elif s[i] == " ":
            answer += " "
            count = 0
    return answer