def solution(n, s):
    # 1로만 이루어진 합으로도 만들지 못하면 만들 수 없는 집합임
    if s < 1*n:
        return [-1]
    # 그럼 여기서 , 해야 할 일은 나머지가 생겼냐 안생겼냐를 확인하면 됨
    # 나머지는 어떻게 처리하는가
    # 나머지는 어쨋든 n보다는 작은 수 n ->6이라면 나머지의 최대는 5 이거를 2또는 1로 만들어주면 최선
    a = s//n
    b = s%n
    answer = [a]*n
    for i in range(b):
        answer[i] += 1
    answer.sort()
    
    return answer