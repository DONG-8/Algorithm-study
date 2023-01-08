def solution(arr1, arr2):
    answer = []
    narr2 = []
    for i in range(len(arr2[0])):
        new_arr = []
        for j in range(len(arr2)):
            new_arr.append(arr2[j][i])
        narr2.append(new_arr)
    
    for i in range(len(arr1)):
        arr = []
        for j in range(len(narr2)):
            a = 0
            for z in range(len(narr2[0])):
                a += arr1[i][z]*narr2[j][z]
            arr.append(a)
        answer.append(arr)
    return answer