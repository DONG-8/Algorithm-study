def solution(s):
    arr = s.split(" ")
    answer = []
    for i in range(len(arr)):
        a = arr[i][:1]
        b = arr[i][1:]
        k = a.upper() + b.lower() + " "
        answer.append(k)
    new = "".join(answer)[:-1]
    
    return new