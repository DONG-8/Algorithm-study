def solution(numbers):
    answer = []
    
    numbers.sort()
    arr = [0]*1000
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            a = numbers[i] + numbers[j]
            if arr[a] == 0:
                arr[a] = 1
                answer.append(a)
    
    answer.sort()
    return answer