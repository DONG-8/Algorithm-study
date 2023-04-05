def solution(s):
    length = len(s)
    max_length = 1
    while length > 1:
        if length <= max_length:
            break
        for i in range(len(s)-length+1):
            if s[i:i+length] == s[i:i+length][::-1]:
                max_length = max(max_length,length)
        length -= 1
    
    return max_length