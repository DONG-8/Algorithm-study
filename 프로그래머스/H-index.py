 def solution(citations):
    answer = 0
    #h 회 이상 인용된 논문의 갯수 파악

#     citations.sort()
#     number = list( set(citations))
#     number_visit = [-1]*len(number)
#     k = 0
#     for i in range(len(citations)):
#         if number_visit[k] == -1 and number[k] == citations[i]:
#             number_visit[k] = i
#             k += 1
    
#     for i in range(len(number_visit)):
#         under_length, upper_length = len(citations[:number_visit[i]]), len(citations[number_visit[i]:])
#         print(under_length, upper_length,citations[:number_visit[i]],citations[number_visit[i]:])
#         if under_length <= upper_length:
#             answer = number[i]
#         else:
#             break
    
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if v <= i:
            return i
    
    
    return len(citations)