def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1],-x[0]))
    number_list = []
    for i in range(row_begin-1,row_end):
        number = 0
        for num in data[i]:
            number += (num % (i+1))
        answer ^= number
    return answer