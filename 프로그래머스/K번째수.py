def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        i,j,k = commands[i]
        slice_arr = array[i-1:j]
        slice_arr.sort()
        # print(slice_arr)
        return_number = slice_arr[k-1]
        # print(return_number)
        answer.append(return_number)

    return answer