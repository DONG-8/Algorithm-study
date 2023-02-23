def solution(s):
    answer = True
    word = "abcdefghijklmnopqrstuvwxyz"
    if len(s) == 4 or len(s) ==6:
        for w in s:
            if w.lower() in word:
                return False
        else:
            return True
    else:
        return False