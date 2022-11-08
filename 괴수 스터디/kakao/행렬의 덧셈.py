def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        k = []
        for j in range(len(arr1[i])):
            a = arr1[i][j] + arr2[i][j]
            k.append(a)
        answer.append(k)
    return answer