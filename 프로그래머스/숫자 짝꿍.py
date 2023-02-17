def solution(X, Y):
    answer = 0
    x = {}
    y = {}
    # dic으로 표현
    for i in X:
        x[i] = x.get(i,0) + 1
    
    for j in Y:
        y[j] = y.get(j, 0) + 1
        
    arr = []
    for num,count in x.items():
        y_number = y.get(num,0)
        if y_number != 0:
            arr += [num] * min(y_number, count)
    if arr == []:
        return "-1"

    if arr.count("0") == len(arr):
        return  "0"
    arr.sort(reverse = True)

    return "".join(arr)